import roles
class Player():
    def __init__(self, name, id, role):
        self.name = name
        self.id = id # 0 to len(num_players)-1
        self.role_class = roles.RoleClass(role) # assign role as RoleClass
        self.role = role
        self.team = role_class.team # assign team, Team.GOOD or Team.BAD
        self.card = role_class.card

        self.sees = role_class.sees.copy()