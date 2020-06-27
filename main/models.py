from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Entry(models.Model):
    employee = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    revenue = models.DecimalField(max_digits=9, decimal_places=2)
    revenuePerHour = models.DecimalField(max_digits=9, decimal_places=2)
    bestBuyCards = models.IntegerField()
    totalTechSupport = models.DecimalField(max_digits=9, decimal_places=2)
    geekSquadSolutions = models.DecimalField(max_digits=9, decimal_places=2)
    officeAttach = models.IntegerField()
    dateCreated = models.DateTimeField(default=timezone.now)


class Goal(models.Model):
    revenue = models.DecimalField(max_digits=9, decimal_places=2)
    revenuePerHour = models.DecimalField(max_digits=9, decimal_places=2)
    bestBuyCards = models.IntegerField()
    totalTechSupport = models.DecimalField(max_digits=9, decimal_places=2)
    geekSquadSolutions = models.DecimalField(max_digits=9, decimal_places=2)
    officeAttach = models.IntegerField()
    dateCreated = models.DateTimeField(default=timezone.now)