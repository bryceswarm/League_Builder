# League Builder script
#
# ** Read a CSV file of player names and skill,
# ** sort them onto 3 teams of equal experience,
# ** Write a roster of teams,
# ** Write letters to players guardians
#
# Author: Bryce Swarm
#


import csv

# read CSV and return Dictionaries
file_name = "/Users/Swarm/Desktop/Bryce's stuff/Treehouse TechDegree/Python/Soccer League/League_Builder/soccer_players.csv"
team_names = ['Dragons', 'Sharks', 'Raptors', 'Dolphins']
practice_time = 'August 17th, at 3:30pm'

def get_player_data(filename):
    with open(filename) as csvfile:
        player_file = csv.DictReader(csvfile)
        return list(player_file)

# sort players based on experience
def get_player_exp(playerlist, experience):
    sorted_players = []
    for player in playerlist:
        if player['Soccer Experience'] == experience:
            sorted_players.append(player)
    return sorted_players

# create teams and assign players
def get_teams(experience_level, team_list):
    players_with_team = []
    for num, player in enumerate(experience_level):
        teamnum = num % len(team_names)
        player['Team'] = team_list[teamnum]
        players_with_team.append(player)
    return players_with_team


def write_team_file(players):
    with open('teams.txt', 'w') as f:
        for team in team_names:
            _write_team(f, team, [p for p in players if p['Team'] == team])

def _write_team(file_descriptor, team_name, players):
    file_descriptor.write("{0}\n---------------------\n".format(team_name))
    for player in players:
        file_descriptor.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**player))
    file_descriptor.write('\n')

# create letters to guardians
def write_guardian_letters(teams):
    for player in teams:
        letter = 'Dear {guardian},\n\n ' \
                '{playername} has been drafted to the {teamname}.\nThe first practice will be on {practice}.' \
                '\nPlease arrive 15 minutes prior to start of practice for jersey distribution.\n\n' \
                'Thank you,\n' \
                'Bryce Swarm\n' \
                'League Commissioner'.format(guardian = player['Guardian Name(s)'], playername = player['Name'], teamname = player['Team'], practice = practice_time)
        letter_file_name = player['Name'].lower().replace(' ', '_') + '.txt'
        letter_file = open(letter_file_name, 'w')
        letter_file.write(letter)


if __name__ == '__main__':
    # Read CSV and return Dictionary of player list
    player_list = get_player_data(file_name)

    # sort inexperienced vs experienced players
    experienced_player = get_player_exp(player_list, 'YES')
    inexperienced_player = get_player_exp(player_list, 'NO')

    # create teams and assign players and combine back into one
    experienced_player = get_teams(experienced_player, team_names)
    inexperienced_player = get_teams(inexperienced_player, team_names)
    assigned_teams = experienced_player + inexperienced_player
    print(assigned_teams)
    # create team rosters file 'teams.txt'
    write_team_file(assigned_teams)

    # create letters to guardians
    write_guardian_letters(assigned_teams)