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
        self.teams.sort(key=lambda team: (-team.points, -(team.goals_for - team.goals_against), team.name))

    def write_league_table(self, filename):
        self.sort_league_teams()  # Ensure teams are sorted before writing
        file = open(filename, 'w')
        # Write the header
        file.write("Rank\tTeam\tWins\tLosses\tDraws\tGF\tGA\tPoints\n")
        last_rank = 1
        last_points = None
        last_goal_diff = None
        for index, team in enumerate(self.teams):
            if (team.points != last_points or (team.goals_for - team.goals_against) != last_goal_diff):
                last_rank = index + 1  # Update rank only if scores or goal difference change
            last_points = team.points
            last_goal_diff = team.goals_for - team.goals_against
            file.write(f"{last_rank}\t{team.name}\t{team.wins}\t{team.losses}\t{team.draws}\t{team.goals_for}\t{team.goals_against}\t{team.points}\n")
        file.close()
        


sample_league = FootballLeague("Sample League")
sample_league.add_league_teams("SampleLeague.txt")
sample_league.write_league_table("'wtan480.txt'")
print_contents("'wtan480.txt'")