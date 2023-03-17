from django.db import models

# Create your models here.
class Match(models.Model):
    date = models.DateField()
    time = models.DateTimeField()