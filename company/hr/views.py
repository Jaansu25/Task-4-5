from rest_framework import viewsets
from .models import Department, Employee, LeaveApplication
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    LeaveApplicationSerializer,
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all().order_by('id')
    serializer_class = LeaveApplicationSerializer

from django.shortcuts import render

# Create your views here.
