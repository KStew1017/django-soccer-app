import requests
import json


def get_players(req):
    response = requests.get(f'{req}')

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None

    roster = []

    for player in data['athletes']:

        player_name = player['displayName']
        player_number = player.get('jersey')

        position = player['position']

        for p in position:
            player_position = position.get('name')

        players = {}
        players['name'] = player_name
        players['number'] = player_number
        players['position'] = player_position

        roster.append(players)

    return roster


def get_teams(req):
    response = requests.get(f'{req}')

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
    
    teams = []
    i = 0

    for team in teams_list:
        team_dict = {}

        team_dict['abbreviation'] = teams_list[i][0]
        team_dict['name'] = teams_list[i][1]
        team_dict['primary_color'] = teams_list[i][2]
        team_dict['secondary_color'] = teams_list[i][3]
        teams.append(team_dict)

        i += 1

    
    # print(teams_list)
    print(teams)



get_teams('http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams')