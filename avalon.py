import card_images
import time
from player import Player
from game import AvalonGame

def start_game():
    """ Starts game, takes player input and initializes and returns AvalonGame objects with players and roles assigned. """
    print("\033[0mStart game!\033[0m\033c")
    time.sleep(1)
    try:
        num_players = int(input("Please enter number of players in the game (5-10): "))
    except ValueError:     
        num_players = 0 
        while not 5 <= num_players <= 10: # validate number of players   
            try:
                num_players = int(input("Invalid input. Please enter number of players in the game as a number (5-10): "))
            except ValueError:
                num_players = 0

    curr_game = AvalonGame(num_players)

    for i in range(num_players):
        id = i
        name = input("Please enter a name for Player {} (unique is preferred): ".format(str(i+1)))
        curr_game.add_player(id, name)
    return curr_game

def instructions():
    print("\033c\nWelcome to Avalon!\n")
    print("Avalon is a game of hidden loyalty. Players are either Loyal Servants of Arthur fighting for the Goodness or aligned with the Evil ways of Mordred. Evil wins if three Quests fail or by assassinating Merlin at the end of the game. Good wins by letting at least three Quests pass and by not letting Merlin be assassinated at the end of the game.\n")
    print("When it is your turn to see the screen, the screen will refresh and display your name and player ID at the top. When you see the next player, please pass on the device.\n")
    print("To enter in a list of players, type out a comma-separated list of IDs, i.e. '1, 3, 5'\n")
    # TODO: enable hints in game
    input("Press Enter when you're ready to begin!")


if __name__ == '__main__':
    game = start_game()