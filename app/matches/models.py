from django.db import models
import datetime

# Create your models here.
class Match(models.Model):
    date_time = models.DateTimeField(null=True)
    location = models.CharField(max_length=64, default='TBD')
    matchup = models.CharField(max_length=32, default='TBD')
    home_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, default='TBD', related_name='home_team', to_field='abbreviation')
    home_team_logo = models.CharField(max_length=1000, null=True)
    home_team_color = models.CharField(max_length=64, default='TBD')
    away_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, default='TBD', related_name='away_team', to_field='abbreviation')
    away_team_logo = models.CharField(max_length=1000, null=True)
    away_team_color = models.CharField(max_length=64, default='TBD')
    home_team_goals = models.PositiveSmallIntegerField(default=0)
    away_team_goals = models.PositiveSmallIntegerField(default=0)
    competition_stage = models.CharField(max_length=64, default='TBD')
    winner = models.CharField(max_length=64, default='draw')
    home_team_abbreviation = models.CharField(max_length=3, default='TBD')
    away_team_abbreviation = models.CharField(max_length=3, default='TBD')
    
    def __str__(self):
        return self.matchup