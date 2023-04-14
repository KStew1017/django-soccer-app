from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'id', 
            'date_time', 
            'location', 
            'matchup', 
            'home_team', 
            'home_team_logo', 
            'home_team_color', 
            'home_team_goals', 
            'away_team', 
            'away_team_color', 
            'away_team_logo', 
            'away_team_goals', 
            'competition_stage', 
            'winner',
            'away_team_name',
            'home_team_name',
            'home_team_recent_form',
            'away_team_recent_form',
            'home_team_champions_league_record',
            'away_team_champions_league_record',
            'home_team_scorers',
            'away_team_scorers'
            )