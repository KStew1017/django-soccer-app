from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from teams.models import Team
from results.models import Result
from players.models import Player
from matches.models import Match


def HomePage(request):
    
    teams_output = Team.objects.all()
    players_output = Player.objects.all()
    matches_output = Match.objects.all()
    results_output = Result.objects.all()

    return render(request, 'home.html', context={
        'teams': teams_output,
        'players': players_output,
        'matches': matches_output,
        'results': results_output
        }
    )