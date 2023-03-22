from django.db import models

# Create your models here.
class Result(models.Model):
    match = models.OneToOneField('matches.Match', on_delete=models.CASCADE)
    home_team_goals = models.PositiveSmallIntegerField(default=0)
    away_team_goals = models.PositiveSmallIntegerField(default=0)
    winner = models.CharField(max_length=64, default='draw')

    def __str__(self):
        return self.name