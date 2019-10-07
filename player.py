import roles
class Player():
    def __init__(self, name, id, role):
        self.name = name
        self.id = id # 0 to len(num_players)-1
        self.role = role # assign role
        self.team = role # assign team, Team.GOOD or Team.BAD