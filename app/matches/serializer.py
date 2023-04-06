from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'date_time', 'location', 'matchup', 'home_team', 'home_team_logo', 'home_team_color', 'home_team_goals', 'away_team', 'away_team_color', 'away_team_logo', 'away_team_goals', 'competition_stage', 'winner')
