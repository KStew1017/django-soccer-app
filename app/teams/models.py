from django.db import models

# Create your models here.
class Team(models.Model):
    abbreviation = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=64, default='', unique=True)
    primary_color = models.CharField(max_length=6, default='ffffff')
    secondary_color = models.CharField(max_length=6, default='ffffff')
    logo_url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name