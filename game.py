from roles import Role
import random
from player import Player

# static dictionary to assign required number of players per quest
players_per_quest = {
    5: [2, 3, 2, 3, 3],
    6: [2, 3, 4, 3, 4],
    7: [2, 3, 3, 4, 4],
    8: [3, 4, 4, 5, 5],
    9: [3, 4, 4, 5, 5],
    10: [3, 4, 4, 5, 5]
}

# assigning roles for each game size
roles_per_game_size = {
    5: [Role.MERLIN, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA],
    6: [Role.MERLIN, Role.PERCIVAL, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA],
    7: [Role.MERLIN, Role.PERCIVAL, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA, Role.OBERON],
    8: [Role.MERLIN, Role.PERCIVAL, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA, Role.MORDRED],
    9: [Role.MERLIN, Role.PERCIVAL, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA, Role.MORDRED],
    10: [Role.MERLIN, Role.PERCIVAL, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.LOYAL_SERVANT, Role.ASSASSIN, Role.MORGANA, Role.MORDRED, Role.OBERON],
}

class AvalonGame():
    def __init__(self, num_players):
        self.num_players = num_players # stores number of players in the game, 5-10
        self.in_progress = True
        self.game_roles_left = self.get_roles()
        self.players_by_id = []
        self.current_round = 1

    def get_roles(self):
        """ Get roles for each game size as an array. """
        return roles_per_game_size[self.num_players]

    def add_player(self, id, name):
        """ Returns a list of length num_players with shuffled roles for each player. """
        if len(self.game_roles_left) > 0:
            idx = random.randint(0, len(self.game_roles_left)-1)
            role = self.game_roles_left.pop(idx)
            self.players_by_id.append(Player(name, id, role))
        else:
            raise ValueError("No roles left!")

    # def run_team_proposal(self):
    #     for i in self.players_by_id:


