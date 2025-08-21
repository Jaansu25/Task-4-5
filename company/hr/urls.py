from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, LeaveApplicationViewSet


router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'leave-applications', LeaveApplicationViewSet, basename='leaveapplication')


urlpatterns = [
    path('', include(router.urls)),
]

