from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=64)
    number = models.PositiveSmallIntegerField(unique=True)
    position = models.CharField(max_length=32)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.name