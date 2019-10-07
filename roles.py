from enum import Enum
import card_images

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

# dictionary mapping role to (team, sees, card)
roles_and_teams = {
    Role.ASSASSIN: (Team.EVIL, [Role.MORGANA, Role.MORDRED], card_images.ASSASSIN_CARD),
    Role.LOYAL_SERVANT: (Team.GOOD, [], card_images.LOYAL_SERVANT_CARD),
    Role.MERLIN: (Team.GOOD, [Role.MORGANA, Role.OBERON, Role.ASSASSIN], card_images.MERLIN_CARD),
    Role.MORGANA: (Team.EVIL, [Role.MORDRED, Role.ASSASSIN], card_images.MORGANA_CARD),
    Role.MORDRED: (Team.EVIL, [Role.MORGANA, Role.ASSASSIN], card_images.MORDRED_CARD),
    Role.OBERON: (Team.EVIL, [], card_images.OBERON_CARD),
    Role.PERCIVAL: (Team.GOOD, [Role.MORGANA, Role.MERLIN], card_images.PERCIVAL_CARD)
}

class RoleClass:
    def __init__(self, role):
        self.role = role # role enum

        self.sees = roles_and_teams[role][1] # array of other members this person sees
        self.team = roles_and_teams[role][0] # team enum value describing good or evil

        self.card = roles_and_teams[role][2]
