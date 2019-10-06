import card_images
import time

class AvalonGame():
    def __init__(self, num_players):
        self.num_players = num_players # stores number of players in the game, 3-8

    def get_roles(self):
        """ Get roles for each game size. """
        pass
        

class Player():
    def __init__(self, name):
        self.name = name

def start_game():
    print("\033[0mStart game!\033[0m\033c")
    time.sleep(1)
    try:
        num_players = int(input("Please enter number of players in the game (3-8): "))
    except ValueError:     
        num_players = 0 
        while not 3 <= num_players <= 8: # validate number of players   
            try:
                num_players = int(input("Invalid input. Please enter number of players in the game (3-8): "))
            except ValueError:
                num_players = 0

    for i in range(num_players):
        input("Please enter a name for Player {} (unique is preferred): ".format(str(i+1)))
    
    return num_players

def instructions():
    print("\033c\nWelcome to Avalon!\n")
    print("Avalon is a game of hidden loyalty. Players are either Loyal Servants of Arthur fighting for the Goodness or aligned with the Evil ways of Mordred. Evil wins if three Quests fail or by assassinating Merlin at the end of the game. Good wins by letting at least three Quests pass and by not letting Merlin be assassinated at the end of the game.\n")
    print("When it is your turn to see the screen, the screen will refresh and display your name and player ID at the top. When you see the next player, please pass on the device.\n")
    # TODO: enable hints in game
    input("Press Enter when you're ready to begin!")





if __name__ == '__main__':
    start_game()