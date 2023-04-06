import requests
import json
import psycopg2
import time
import unicodedata
import datetime


### debug ###
#
# players = http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams/382/roster
# teams = http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams
# matches = http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates=20220906-20220907
#
### debug ###

############## API REQUESTS ##############

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:
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
        player_name = player_name.replace("'", "''")
        if player.get('jersey') == None:
            player_number = 0
        else:
            player_number = player.get('jersey')
        player_position = player.get('position')['name']

        players = []
        players.append(player_name)
        players.append(player_number)
        players.append(player_position)

        roster.append(players)
    
    for player in roster:
        team = data['team'].get('abbreviation')
        player.append(team)

    return roster


def get_teams(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None

    teams = []

    for team in data['sports'][0]['leagues'][0]['teams']:
        abbreviation = team.get('team')['abbreviation']
        name = team.get('team')['name']
        name = strip_accents(name)
        primary_color = team.get('team')['color']
        secondary_color = team.get('team')['alternateColor']
        logo_url = team.get('team')['logos'][0]['href']

        team_data = []
        team_data.append(abbreviation)
        team_data.append(name)
        team_data.append(primary_color)
        team_data.append(secondary_color)
        team_data.append(logo_url)
    
        teams.append(team_data)

    return teams


def get_matches(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None
    
    matches = []

    for match in data['events']:
        date_time = match.get('date')
        location = match.get('competitions')[0]['venue']['fullName']
        matchup = match.get('shortName')
        home_team = match.get('competitions')[0]['competitors'][0]['team']['abbreviation']
        home_team_logo = match.get('competitions')[0]['competitors'][0]['team']['logo']
        home_team_color = match.get('competitions')[0]['competitors'][0]['team']['color']
        home_team_goals = match.get('competitions')[0]['competitors'][0]['score']
        away_team = match.get('competitions')[0]['competitors'][1]['team']['abbreviation']
        away_team_logo = match.get('competitions')[0]['competitors'][1]['team']['logo']
        away_team_color = match.get('competitions')[0]['competitors'][1]['team']['color']
        away_team_goals = match.get('competitions')[0]['competitors'][1]['score']
        competition_stage = match.get('season')['slug']

        if competition_stage == 'group-stage':
            competition_stage = 'Group Stage'
        elif competition_stage == 'round-of-16':
            competition_stage = 'Round of 16'
        elif competition_stage == 'quarterfinals':
            competition_stage = 'Quarterfinals'
        elif competition_stage == 'semifinals':
            competition_stage = 'Semifinals'
        elif competition_stage == 'finals':
            competition_stage = 'Finals'
        
        if match.get('competitions')[0]['competitors'][0]['winner'] is True:
            winner = match.get('competitions')[0]['competitors'][0]['team']['abbreviation']
        elif match.get('competitions')[0]['competitors'][1]['winner'] is True:
            winner = match.get('competitions')[0]['competitors'][1]['team']['abbreviation']
        else:
            winner = 'Draw'

        date1 = datetime.datetime.utcnow()
        date2 = date1.replace(microsecond=0, second=0)
        date3 = date2.strftime('%Y-%m-%dT%H:%M:%S')
        datetime_now = date3[:-3] + 'Z'

        if date_time > datetime_now:
            winner = 'TBD'

        match_data = []
        match_data.append(date_time)
        match_data.append(location)
        match_data.append(matchup)
        match_data.append(competition_stage)
        match_data.append(home_team)
        match_data.append(away_team)
        match_data.append(home_team_goals)
        match_data.append(away_team_goals)
        match_data.append(home_team_logo)
        match_data.append(away_team_logo)
        match_data.append(home_team_color)
        match_data.append(away_team_color)
        match_data.append(winner)

        matches.append(match_data)

    return matches


def get_team_ids(req):
    response = requests.get(req)

    if (response and response.status_code) == 200:
        data = response.json()
    else:
        None

    team_ids = []

    for team in data['sports'][0]['leagues'][0]['teams']:
        team_id = team.get('team')['id']
        team_ids.append(team_id)

    return team_ids


def match_dates():
    matchday1 = '20220906-20220907'
    matchday2 = '20220913-20220914'
    matchday3 = '20221004-20221005'
    matchday4 = '20221011-20221012'
    matchday5 = '20221025-20221026'
    matchday6 = '20221101-20221102'
    r16_1st_dates = '20230214-20230222'
    r16_2nd_dates = '20230307-20230315'
    qf_1st_dates = '20230411-20230412'
    qf_2nd_dates = '20230418-20230419'
    sf_1st_dates = '20230420-20230701'
    sf_2nd_dates = '20230420-20230701'
    final_dates = '20230420-20230701'

    matchdays = []

    matchdays.append(matchday1)
    matchdays.append(matchday2)
    matchdays.append(matchday3)
    matchdays.append(matchday4)
    matchdays.append(matchday5)
    matchdays.append(matchday6)
    matchdays.append(r16_1st_dates)
    matchdays.append(r16_2nd_dates)
    matchdays.append(qf_1st_dates)
    matchdays.append(qf_2nd_dates)
    matchdays.append(sf_1st_dates)
    matchdays.append(sf_2nd_dates)
    matchdays.append(final_dates)

    return matchdays

############## SEED FUNCTIONS ##############

def seed_teams():
    conn = psycopg2.connect(
        """
        dbname=soccerapp_db user=postgres host=pg port=5432
        """
    )

    conn.set_session(autocommit=True)
    cur = conn.cursor()

    team_data = get_teams('http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams')

    for team in team_data:
        cur.execute(
            f"""
            INSERT INTO teams_team (abbreviation, name, primary_color, secondary_color, logo_url)
            VALUES ('{team[0]}', '{team[1]}', '{team[2]}', '{team[3]}', '{team[4]}')
            """
        )


def seed_players():
    conn = psycopg2.connect(
        """
        dbname=soccerapp_db user=postgres host=pg port=5432
        """
    )

    conn.set_session(autocommit=True)
    cur = conn.cursor()

    team_ids = get_team_ids('http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams')

    for team_id in team_ids:
        player_data = get_players(f'http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams/{team_id}/roster')

        for player in player_data:
            cur.execute(
                f"""
                INSERT INTO players_player (name, number, position, team)
                VALUES ('{player[0]}', '{player[1]}', '{player[2]}', '{player[3]}')
                """
            )


def seed_matches():
    conn = psycopg2.connect(
        """
        dbname=soccerapp_db user=postgres host=pg port=5432
        """
    )

    conn.set_session(autocommit=True)
    cur = conn.cursor()

    matchdays = match_dates()

    for matchday in matchdays:
        match_data = get_matches(f'http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates={matchday}')

        for match in match_data:
            cur.execute(
                f"""
                INSERT INTO matches_match (date_time, location, matchup, competition_stage, home_team_id, away_team_id, home_team_goals, away_team_goals, home_team_logo, away_team_logo, home_team_color, away_team_color, winner)
                VALUES ('{match[0]}', '{match[1]}', '{match[2]}', '{match[3]}', '{match[4]}', '{match[5]}', '{match[6]}', '{match[7]}', '{match[8]}', '{match[9]}', '{match[10]}', '{match[11]}', '{match[12]}')
                """
            )


seed_teams()
seed_players()
seed_matches()
