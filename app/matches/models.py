from django.db import models
import datetime

# Create your models here.
class Match(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=64, default='TBD')
    matchup = models.CharField(max_length=32, default='TBD')
    home_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, default='TBD', related_name='home_team', db_column='home_team', to_field='abbreviation')
    away_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, default='TBD', related_name='away_team', db_column='away_team', to_field='abbreviation')
    competition_stage = models.CharField(max_length=64, default='TBD')
    
    def __str__(self):
        return self.name