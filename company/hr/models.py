from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    baseSalary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self) -> str:
        return f"{self.name}"


class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_applications')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self) -> str:
        return f"LeaveApplication({self.employee_id}) {self.start_date} -> {self.end_date}"
