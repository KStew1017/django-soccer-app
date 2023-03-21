from django.db import models

# Create your models here.
class Match(models.Model):
    date = models.DateField()
    time = models.DateTimeField()
    home_team = models.CharField(max_length=64)
    away_team = models.CharField(max_length=64)