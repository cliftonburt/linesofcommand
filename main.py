from game_loop import run_game
from player import Player

def main():
    """
    Main entry point for the Lines of Command game.
    """
    print("Welcome to Lines of Command!")
    player = Player(name="Captain")  # Initialize player with default name
    run_game(player)  # Start the main game loop

if __name__ == "__main__":
    main()