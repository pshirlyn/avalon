from enum import Enum

# dictionary mapping role to (team, sees, visible_to, card)
roles_and_teams = {
    Role.ASSASSIN: (Team.EVIL, [], ),
    Role.EVIL_MINION: (Team.EVIL, []),
    Role.LOYAL_SERVANT: (Team.GOOD, []),
    Role.MERLIN: (Team.GOOD, [Role.MORGANA, Role.OBERON]),
    Role.MORGANA: (Team.EVIL),
    Role.MORDRED: (Team.EVIL),
    Role.OBERON: (Team.EVIL),
    Role.PERCIVAL: (Team.GOOD, [Role.MORGANA, Role.MERLIN], [], )
}

class Team(Enum):
    GOOD = 1
    EVIL = 2

class Role(Enum):
    MERLIN = 1
    LOYAL_SERVANT = 2
    PERCIVAL = 3
    MORGANA = 4
    MORDRED = 5
    OBERON = 6
    ASSASSIN = 7
    EVIL_MINION = 8

class RoleClass:
    def __init__(self, role):
        self.role = role # role enum

        self.sees = roles_and_teams[1] # array of other members this person sees
        # self.visible_to = visible_to[2] # array of other members this person is visible to
        self.team = team[0] # team enum value describing good or evil

        self.card = roles_and_teams[3]

    def is_good(self):
        return self.team == Team.GOOD
