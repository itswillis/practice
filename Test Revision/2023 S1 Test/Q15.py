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
        return (f'{self.name}\t\t{self.wins}\t{self.draws}\t{self.losses}\t{self.goals_for}\t{self.goals_against}\t{self.points}')

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
    
    def sort_league_teams(self):
        # team is ranked higher than another team if it has more points
        # if it has the same number of points then goal difference is considered (goals for - goals against) -> larger goal difference is higher ranked 
        # if two teams have the same number of points and goal difference, sort alphabetically. 
        for teams in range(len(self.teams) -1, 0, -1):
            position_largest = 0
            for i in range(1, teams):
                if self.teams[i].points < self.teams[position_largest].points:
                    position_largest = i
            if self.teams[position_largest].points < self.teams[teams].points: 
                self.teams[position_largest], self.teams[teams] = self.teams[teams], self.teams[position_largest]
            
            # if it has the same number of points
            if self.teams[position_largest].points == self.teams[teams].points: 
                # higher goal difference is higher ranked
                if (self.teams[position_largest].goals_for - self.teams[position_largest].goals_against) < (self.teams[teams].goals_for - self.teams[teams].goals_against):
                    self.teams[position_largest], self.teams[teams] = self.teams[teams], self.teams[position_largest]
                    # if its the same 
                elif (self.teams[position_largest].goals_for - self.teams[position_largest].goals_against) == (self.teams[teams].goals_for - self.teams[teams].goals_against):
                    if self.teams[i].name < self.teams[position_largest].name:
                        position_largest = i
                    

sample_league = FootballLeague("La Liga")
sample_league.add_league_teams("League1a.txt")
sample_league.sort_league_teams()
for team in sample_league.teams:
    print(team)