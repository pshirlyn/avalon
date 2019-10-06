import unittest
import avalon

class TestAvalonGame(unittest.TestCase):

    def test_game_setup(self):
        avalon.start_game()

    def test_instructions(self):
        avalon.instructions()

if __name__ == "__main__":
    unittest.main()

