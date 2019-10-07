import unittest
import avalon
from game import AvalonGame

class TestAvalonGame(unittest.TestCase):

    def test_game_setup(self):
        game = avalon.start_game()
        for player in game.players_by_id:
            print(player.name, player.id, player.role)

    def test_instructions(self):
        avalon.instructions()

    def test_game_object(self):
        game = AvalonGame(5)
        roles = game.get_roles()
        assert len(roles) == game.num_players
        random_roles = game.randomly_assign_roles()
        assert len(random_roles) == game.num_players

    def test_voting(self):
        test_game = AvalonGame(5)
        for i in range(5):
            id = i
            name = "test_player_"+str(i)
            test_game.add_player(id, name)
        test_game.run_team_proposal(1)

    def test_quest_run(self):
        test_game = AvalonGame(5)
        for i in range(5):
            id = i
            name = "test_player_"+str(i)
            test_game.add_player(id, name)
        test_team = [test_game.players_by_id[0], test_game.players_by_id[1]]
        print(test_game.run_quest(test_team, 1))
        

if __name__ == "__main__":
    unittest.main()

