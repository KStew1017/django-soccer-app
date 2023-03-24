import requests
import json
import psycopg2
import time
import unicodedata


def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)


def get_players(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None

    roster = []

    for player in data['athletes']:

        player_name = player.get('displayName')
        player_name = strip_accents(player_name)
        player_number = player.get('jersey')

        position = player.get('position')

        for p in position:
            player_position = position.get('name')

        players = []
        players.append(player_name)
        players.append(player_number)
        players.append(player_position)

        roster.append(players)
    
    for player in roster:
        team = data['team'].get('abbreviation')
        player.append(team)

    data = json.dumps(roster, indent=4)
    return data


def get_teams(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None

    get_abbreviation = lambda team_dict: team_dict['team']['abbreviation']
    abbreviations = map(get_abbreviation, data['sports'][0]['leagues'][0]['teams'])
    abbreviations = list(abbreviations)

    get_name = lambda team_dict: team_dict['team']['name']
    names = map(get_name, data['sports'][0]['leagues'][0]['teams'])
    names = list(names)

    get_primary_color = lambda team_dict: team_dict['team']['color']
    primary_colors = map(get_primary_color, data['sports'][0]['leagues'][0]['teams'])
    primary_colors = list(primary_colors)

    get_secondary_color = lambda team_dict: team_dict['team']['alternateColor']
    secondary_colors = map(get_secondary_color, data['sports'][0]['leagues'][0]['teams'])
    secondary_colors = list(secondary_colors)

    teams_list = list(zip(abbreviations, names, primary_colors, secondary_colors))
    
    data = json.dumps(teams_list, indent=4)
    return data


def get_matches(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None
    
    





























# def seed_teams():
#     conn = psycopg2.connect(
#         """
#         dbname=soccerapp_db user=postgres host=localhost port=5432
#         """
#     )

#     conn.set_session(autocommit=True)
#     cur = conn.cursor()

#     team_data = get_teams('http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams')

#     for team in team_data:
#         cur.execute(
#             f"""
#             INSERT INTO teams_team (abbreviation, name, primary_color, secondary_color)
#             VALUES ('{team[0]}', '{team[1]}', '{team[2]}', '{team[3]}')
#             """
#         )