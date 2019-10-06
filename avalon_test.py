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

if __name__ == "__main__":
    unittest.main()

