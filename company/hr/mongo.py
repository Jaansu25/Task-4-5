import os
from typing import Any, Dict

from pymongo import MongoClient


_client: MongoClient | None = None


def _get_mongo_client() -> MongoClient:
    global _client
    if _client is None:
        uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')
        _client = MongoClient(uri)
    return _client


def _get_chat_collection():
    client = _get_mongo_client()
    db_name = os.environ.get('MONGODB_DB_NAME', 'company_chat')
    collection = client[db_name]['chat_messages']
    # Ensure helpful indexes (idempotent)
    try:
        collection.create_index('group')
        collection.create_index([('group', 1), ('timestamp', -1)])
    except Exception:
        # Index creation failures should not break message saving in dev
        pass
    return collection


def save_chat_message_sync(document: Dict[str, Any]) -> None:
    """Insert a chat message document into MongoDB synchronously.

    Expected keys include: group (partition key), department_id, message,
    timestamp, sender, and optionally employee_id.
    """
    collection = _get_chat_collection()
    collection.insert_one(document)

