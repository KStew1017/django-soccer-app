from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id', 
            'name', 
            'number', 
            'position', 
            'nationality', 
            'age', 
            'height', 
            'weight', 
            'team'
            )
