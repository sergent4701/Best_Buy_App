from django.db import models


class Users(models.Model):
    employeeId = models.CharField(max_length=20)
    employeeType = models.CharField(max_length=20)
    salt = models.TextField()
    password = models.TextField()


class Entries(models.Model):
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
