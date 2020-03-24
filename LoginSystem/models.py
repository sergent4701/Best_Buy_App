from django.db import models
from django.util import timezone


class Users(models.Model):
    employeeFirst = models.CharField(max_length=25)
    employeeLast = models.CharField(max_length=25)
    employeeId = models.CharField(max_length=8)
    employeeType = models.TextField()
    salt = models.TextField()
    password = models.TextField()
    dateCreated = models.DateTimeField(default=timezone.now)


class Entries(models.Model):
    revenue = models.DecimalField(max_digits=9, decimal_places=2)
    employee = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
