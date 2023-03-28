from django.shortcuts import render
from teams.models import Team
from players.models import Player
from matches.models import Match


def HomePage(request):
    
    teams_output = Team.objects.all()
    players_output = Player.objects.all()
    matches_output = Match.objects.all()

    return render(request, 'home.html', context={
        'teams': teams_output,
        'players': players_output,
        'matches': matches_output
        }
    )