from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('abbreviation', 'name', 'primary_color', 'secondary_color', 'logo_url')
