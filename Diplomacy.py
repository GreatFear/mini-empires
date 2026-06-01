from Nation import Nation

# Add treaties later

class Diplomacy:

    def __init__(self, nation1_id: int, nation2_id: int):
        self.nation1_id = nation1_id
        self.nation2_id = nation2_id
        self.status = "PEACE"

    def declare_war(self):
        self.status = "WAR"

    def make_peace(self):
        self.status = "PEACE"

    def create_alliance(self):
        self.status = "ALLIED"
