from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=64, default='', unique=True)
    location = models.CharField(max_length=64, default='')
    wins = models.PositiveSmallIntegerField()
    losses = models.PositiveSmallIntegerField()