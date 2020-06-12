from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# class Entries(models.Model):
#     revenue = models.DecimalField(max_digits=9, decimal_places=2)
#     revenuePerHour = models.DecimalField(max_digits=9, decimal_places=2)
#     bestBuyCards = models.IntegerField()
#     totalTechSupport = models.DecimalField(max_digits=9, decimal_places=2)
#     geekSquadSolutions = models.DecimalField(max_digits=9, decimal_places=2)
#     officeAttach = models.IntegerField()
#     employee = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
#     dateCreated = models.DateTimeField(default=timezone.now)
#
#
# class Goals(models.Model):
#     revenue = models.DecimalField(max_digits=9, decimal_places=2)
#     revenuePerHour = models.DecimalField(max_digits=9, decimal_places=2)
#     bestBuyCards = models.IntegerField()
#     totalTechSupport = models.DecimalField(max_digits=9, decimal_places=2)
#     geekSquadSolutions = models.DecimalField(max_digits=9, decimal_places=2)
#     officeAttach = models.IntegerField()
#     dateCreated = models.DateTimeField(default=timezone.now)
