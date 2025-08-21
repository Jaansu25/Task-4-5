from rest_framework import serializers
from .models import Department, Employee, LeaveApplication


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'baseSalary', 'department']


class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = ['id', 'employee', 'start_date', 'end_date', 'reason']

