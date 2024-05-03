class FootballTeam: 
    def __init__(self, name, wins, draws, losses, goals_for, goals_against, points):
        self.name = name 
        self.wins = wins 
        self.draws = draws
        self.losses = losses
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points

    def __str__(self):
        return (f'{self.name}\t\t{self.wins}\t{self.draws}\t 
                {self.losses}\t 
                {self.goals_for}\t 
                {self.goals_against}\t{self.points}')

class FootballLeague:
    def __init__(self, name):
        self.name = name
        self.teams = []
    
    def add_league_teams(self, filename):
        try:
            input_file = open(filename, 'r')
            contents = input_file.read().strip().split("\n")
            for line in contents:
                line = line.strip()  # Remove any extra whitespace
                if line:  # Check if the line is not empty
                    # Parse the team data
                    team_data = line.split(", ")
                    # Create a FootballTeam object
                    team = FootballTeam(
                        name=team_data[0], 
                        wins=int(team_data[1]),
                        draws=int(team_data[2]),
                        losses=int(team_data[3]),
                        goals_for=int(team_data[4]),
                        goals_against=int(team_data[5]),
                        points=int(team_data[6])
                    )
                    # Append the team object to the league's team list
                    self.teams.append(team)
            input_file.close()
        except FileNotFoundError:
            print("ERROR! File not found")

sample_league = FootballLeague("Sample League")
sample_league.add_league_teams("SampleLeague.txt")
for team in sample_league.teams:
    print(team)