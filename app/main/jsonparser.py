import requests
import json
from django.http.response import JsonResponse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

from rest_framework.parsers import JSONParser


def get_players(roster):
    req = requests.get(f'{roster}')
    req = JSONParser().parse(req)
    roster = []

    for player in req.athletes:
        roster.append({"name": player.fullname})

    print(roster)

get_players('http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams/382/roster')