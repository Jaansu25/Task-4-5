import asyncio
import json
from datetime import datetime, timezone

from channels.generic.websocket import AsyncWebsocketConsumer

from .mongo import save_chat_message_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Department primary key is the group name
        self.department_id = self.scope['url_route']['kwargs']['department_id']
        self.group_name = str(self.department_id)

        # Join department group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave department group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data: str | bytes | None):
        if not text_data:
            return

        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            return

        message_text: str = data.get('message', '')
        sender: str | None = data.get('sender')
        employee_id = data.get('employee_id')

        timestamp = datetime.now(timezone.utc)

        # Persist the message in MongoDB with group as partition key
        document = {
            'group': self.group_name,
            'department_id': int(self.department_id),
            'employee_id': employee_id,
            'sender': sender,
            'message': message_text,
            'timestamp': timestamp,
        }
        await asyncio.to_thread(save_chat_message_sync, document)

        # Broadcast to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'sender': sender,
                'employee_id': employee_id,
                'message': message_text,
                'timestamp': timestamp.isoformat(),
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

