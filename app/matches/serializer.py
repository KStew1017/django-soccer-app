from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'date_time', 'location', 'matchup', 'home_team', 'away_team', 'competition_stage')
