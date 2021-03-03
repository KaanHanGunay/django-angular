from django.db import models


class Department(models.Model):
    DepartmentName = models.CharField(max_length=255)
    DepartmentId = models.AutoField(primary_key=True)


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=50)
