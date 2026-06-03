from Nation import Nation

# Add treaties later

class Diplomacy:

    def __init__(self, nation1: Nation, nation2: Nation):
        self.nations = []
        self.nations.append(nation1)
        self.nations.append(nation2)
        self.status = "PEACE"

    # Returns those involved in this diplomacy... Probaby should change this to just straight up treaties
    def get_participants(self):
        return self.nations
    
    def declare_war(self):
        self.status = "WAR"

    def make_peace(self):
        self.status = "PEACE"

    def create_alliance(self):
        self.status = "ALLIED"
