from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'date_time', 'away_team', 'home_team', 'location')
