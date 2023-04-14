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
        if player.get('jersey') is None:
            player_number = 0
        else:
            player_number = player.get('jersey')
        player_position = player.get('position')['name']
        player_nationality = player.get('citizenship')
        player_age = player.get('age')

        if player.get('height') is None:
            player_height = 'No Data'
        else:
            player_height_float = player.get('height')
            player_height_feet = int(player_height_float // 12)
            player_height_inches = int(player_height_float % 12)
            player_height = str(player_height_feet) + ' ft ' + str(player_height_inches) + ' in'

        if player.get('weight') is None:
            player_weight = 'No Data'
        else:
            player_weight = player.get('displayWeight')

        players = []
        players.append(player_name)
        players.append(player_number)
        players.append(player_position)
        players.append(player_nationality)
        players.append(player_age)
        players.append(player_height)
        players.append(player_weight)

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
        home_team_name = match.get('competitions')[0]['competitors'][0]['team']['name']
        home_team_name = strip_accents(home_team_name)
        away_team_name = match.get('competitions')[0]['competitors'][1]['team']['name']
        away_team_name = strip_accents(away_team_name)
        home_team_recent_form = match.get('competitions')[0]['competitors'][0]['form']
        away_team_recent_form = match.get('competitions')[0]['competitors'][1]['form']

        try:
            if match.get('competitions')[0]['competitors'][0]['records'][0]['summary'] is None:
                home_team_champions_league_record = 'No Data'
            else:
                home_team_champions_league_record = match.get('competitions')[0]['competitors'][0]['records'][0]['summary']

            if match.get('competitions')[0]['competitors'][1]['records'][0]['summary'] is None:
                away_team_champions_league_record = 'No Data'
            else:
                away_team_champions_league_record = match.get('competitions')[0]['competitors'][1]['records'][0]['summary']
        except:
            home_team_champions_league_record = 'No Data'
            away_team_champions_league_record = 'No Data'
        
        match_details = match.get('competitions')[0]['details']
        home_team_scorers = []
        away_team_scorers = []
        for event in match_details:
            if ('goal' in event.get('type')['text'].lower()) or ('penalty' in event.get('type')['text'].lower()):
                if event.get('team')['id'] == match.get('competitions')[0]['competitors'][0]['id']:
                    goal = event.get('athletesInvolved')[0]['shortName'] + ' (' + event.get('clock')['displayValue'].replace("'", "") + ')'
                    home_team_scorers.append(goal)
                elif event.get('team')['id'] == match.get('competitions')[0]['competitors'][1]['id']:
                    goal = event.get('athletesInvolved')[0]['shortName'] + ' (' + event.get('clock')['displayValue'].replace("'", "") + ')'
                    away_team_scorers.append(goal)

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
        date2 = date1.replace(microsecond=0, second=0, tzinfo=None)
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
        match_data.append(home_team_name)
        match_data.append(away_team_name)
        match_data.append(home_team_recent_form)
        match_data.append(away_team_recent_form)
        match_data.append(home_team_champions_league_record)
        match_data.append(away_team_champions_league_record)
        match_data.append(home_team_scorers)
        match_data.append(away_team_scorers)

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
            INSERT INTO teams_team (
                abbreviation,
                name,
                primary_color,
                secondary_color,
                logo_url
            )
            VALUES (
                '{team[0]}',
                '{team[1]}',
                '{team[2]}',
                '{team[3]}',
                '{team[4]}'
            )
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
                INSERT INTO players_player (
                    name,
                    number,
                    position,
                    nationality,
                    age,
                    height,
                    weight,
                    team
                )
                VALUES (
                    '{player[0]}',
                    '{player[1]}',
                    '{player[2]}',
                    '{player[3]}',
                    '{player[4]}',
                    '{player[5]}',
                    '{player[6]}',
                    '{player[7]}'
                )
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
                """
                INSERT INTO matches_match (
                    date_time,
                    location, matchup,
                    competition_stage,
                    home_team_id,
                    away_team_id,
                    home_team_goals,
                    away_team_goals,
                    home_team_logo,
                    away_team_logo,
                    home_team_color,
                    away_team_color,
                    winner,
                    home_team_name,
                    away_team_name,
                    home_team_recent_form,
                    away_team_recent_form,
                    home_team_champions_league_record,
                    away_team_champions_league_record,
                    home_team_scorers,
                    away_team_scorers
                )
                VALUES (
                    %(date_time)s,
                    %(location)s,
                    %(matchup)s,
                    %(competition_stage)s,
                    %(home_team_id)s,
                    %(away_team_id)s,
                    %(home_team_goals)s,
                    %(away_team_goals)s,
                    %(home_team_logo)s,
                    %(away_team_logo)s,
                    %(home_team_color)s,
                    %(away_team_color)s,
                    %(winner)s,
                    %(home_team_name)s,
                    %(away_team_name)s,
                    %(home_team_recent_form)s,
                    %(away_team_recent_form)s,
                    %(home_team_champions_league_record)s,
                    %(away_team_champions_league_record)s,
                    %(home_team_scorers)s,
                    %(away_team_scorers)s
                )
                """,
                {
                    'date_time': match[0],
                    'location': match[1],
                    'matchup': match[2],
                    'competition_stage': match[3],
                    'home_team_id': match[4],
                    'away_team_id': match[5],
                    'home_team_goals': match[6],
                    'away_team_goals': match[7],
                    'home_team_logo': match[8],
                    'away_team_logo': match[9],
                    'home_team_color': match[10],
                    'away_team_color': match[11],
                    'winner': match[12],
                    'home_team_name': match[13],
                    'away_team_name': match[14],
                    'home_team_recent_form': match[15],
                    'away_team_recent_form': match[16],
                    'home_team_champions_league_record': match[17],
                    'away_team_champions_league_record': match[18],
                    'home_team_scorers': match[19],
                    'away_team_scorers': match[20],
                }
            )



seed_teams()
seed_players()
seed_matches()
