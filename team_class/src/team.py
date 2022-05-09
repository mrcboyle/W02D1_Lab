class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, name):
        self.players.append(name)
    
    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True
        else: return False
    
    def play_game(self, result):
        if  result == True:
            self.points += 3


# Test - team1 = Team("Codeclan", ["Ewan", "Chris", "Simona"], "Steve")
# Test - print(team1.has_player("Ewan"))