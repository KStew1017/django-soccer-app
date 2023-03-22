from django.db import models

# Create your models here.
class Match(models.Model):
    date_time = models.DateTimeField(null=True)
    home_team = models.ForeignKey('teams.Team', related_name='home_team', on_delete=models.DO_NOTHING, null=True)
    away_team = models.ForeignKey('teams.Team', related_name='away_team', on_delete=models.DO_NOTHING, null=True)
    location = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name