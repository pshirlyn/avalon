import roles
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
        self.curr_active_player = 0 # id of current player proposing

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

    def run_show_roles(self):
        """ Runs revealing card procedure, assuming all players have already been added. """
        input("Now, we reveal everyone's cards individually. One by one, roles will be revealed. When it is your turn, you may look at the screen. Otherwise, please do not look at the screen. Press ENTER to begin.")


    def run_team_proposal(self, quest):
        """ Runs team voting sequence, returns list of team as player objects. """
        decided_team = False
        i = 0
        while True: # loop until we force a team
            # try getting team for quest i+1, voting enabled for all quests but last one
            print("Quest {}, voting round {}\n".format(quest, i+1))
            proposed_team = self.prompt_for_team(self.players_by_id[self.curr_active_player], quest, i+1)
            self.curr_active_player = (self.curr_active_player + 1) % self.num_players # increment player by one, wrap around
            if not proposed_team:
                input("Team failed! Press ENTER to propose new team.")
                i += 1
            else:
                return proposed_team
            

    def prompt_for_team(self, player, quest, voting_round):
        """ Prompt Player Object for a team selection. Return team as array of Players. """
        team = input("\033c\nPlayer {} ({}), please enter in a team of size {} as a list of Player numbers, comma separated.\n".format(player.id+1, player.name, players_per_quest[self.num_players][quest-1]))
        proposed_team = []
        for i in team.split(","):
            player_id = int(i)-1 # parse team player id into array index
            player_obj = self.players_by_id[player_id] # TODO: catch parse errors
            proposed_team.append(player_obj)
        
        # if we're on the last quest (5), force return this team
        if voting_round == 5:
            return proposed_team

        # otherwise try voting round
        num_votes = 0
        for i in self.players_by_id:
            vote = input("\nPlayer {} ({}), please enter Y to vote for this team or N to fail this team: ".format(i.id+1, self.players_by_id[i.id].name))
            if vote == "Y":
                num_votes += 1
        
        if num_votes > self.num_players//2: # majority passes
            return proposed_team
        else: 
            return False


    def run_quest(self, team, round):
        """ Runs quest prompts. Shows to team individually and asks them to vote. Returns True if quest passed or False otherwise. """

        # sets number of failures required to fail this mission
        if round == 4 and self.num_players >= 7:
            failures_required = 2
        else:
            failures_required = 1
        
        input("\033c\nWe now begin the voting process. When the screen displays your name and your player number, you may vote on the quest. Otherwise, do not look at the screen. Press ENTER to begin. ")

        failures = 0
        for p in team:
            vote = input("\033c\nPlayer {} ({}), please enter Y if you want the quest to pass or N if you want the quest to fail. If you are on team GOOD, any vote you enter will be registered as a success. Otherwise, you may choose either option.\n".format(p.id+1, p.name))
            if vote != "Y":
            #if p.team != Team.GOOD and vote != "Y":
                failures += 1
        
        return failures < failures_required

    def failure(self):
        """ Runs when evil team wins the game! """
        pass

    def success(self):
        """ Runs when the good team wins the game! """
        pass
