from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from players.models import Player
from players.serializer import PlayerSerializer
from rest_framework.decorators import api_view


class roster(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'players/index.html'

    def get(self, request, team):
        queryset = Player.objects.filter(team=team)
        return Response({'players': queryset})

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'players/index.html'

    def get(self, request):
        queryset = Player.objects.all()
        return Response({'players': queryset})

@api_view(['GET', 'POST', 'DELETE'])
def players_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        player_serializer = PlayerSerializer(players, many=True)
        return JsonResponse(player_serializer.data, safe=False)
    
    elif request.method == 'POST':
        player_data = JSONParser().parse(request)
        player_serializer = PlayerSerializer(data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse(player_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Player.objects.all().delete()
        return JsonResponse(
            {
                'message': f'{count[0]} players were deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET', 'DELETE', 'PATCH'])
def individual_player(request, id):
    try:
        player = Player.objects.get(pk=id)
    except Player.DoesNotExist:
        return JsonResponse({'message': 'The player does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        player_serializer = PlayerSerializer(player)
        return JsonResponse(player_serializer.data)
    
    elif request.method == 'PATCH':
        player_data = JSONParser().parse(request)
        player_serializer = PlayerSerializer(player, data=player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse(player_serializer.data)
        return JsonResponse(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player.delete()
        return JsonResponse({'message': 'player was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)