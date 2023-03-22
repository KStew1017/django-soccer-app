from rest_framework import serializers
from results.models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'match', 'home_team_goals', 'away_team_goals', 'winner')
