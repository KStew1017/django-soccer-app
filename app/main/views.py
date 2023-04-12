from django.shortcuts import render
from teams.models import Team
from matches.models import Match
from players.models import Player


def HomePage(request):
    
    teams = Team.objects.all()
    matches = Match.objects.all()
    matchday1 = Match.objects.filter(date_time__range=['2022-09-06', '2022-09-07'])
    matchday2 = Match.objects.filter(date_time__range=['2022-09-13', '2022-09-14'])
    matchday3 = Match.objects.filter(date_time__range=['2022-10-04', '2022-10-05'])
    matchday4 = Match.objects.filter(date_time__range=['2022-10-11', '2022-10-12'])
    matchday5 = Match.objects.filter(date_time__range=['2022-10-25', '2022-10-26'])
    matchday6 = Match.objects.filter(date_time__range=['2022-11-01', '2022-11-02'])
    matchday7 = Match.objects.filter(date_time__range=['2023-02-14', '2023-02-22'])
    matchday8 = Match.objects.filter(date_time__range=['2023-03-07', '2023-03-15'])
    matchday9 = Match.objects.filter(date_time__range=['2023-04-11', '2023-04-12'])
    matchday10 = Match.objects.filter(date_time__range=['2023-04-18', '2023-04-19'])

    matchdays = [matchday1, matchday2, matchday3, matchday4, matchday5, matchday6, matchday7, matchday8, matchday9, matchday10]



    return render(request, 'home.html', context={
        'teams': teams,
        'matches': matches,
        'matchdays': matchdays
        }
    )

def TeamPage(request, abbreviation):
    team = Team.objects.get(pk=abbreviation)
    players = Player.objects.filter(team__pk=abbreviation)
    return render(request, 'team.html', context={
        'team': team,
        'players': players
        }
    )