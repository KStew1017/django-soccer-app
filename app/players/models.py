from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=64)
    number = models.PositiveSmallIntegerField(unique=True)
    position = models.CharField(max_length=32)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, db_column='team', to_field='abbreviation')
    
    def __str__(self):
        return self.name