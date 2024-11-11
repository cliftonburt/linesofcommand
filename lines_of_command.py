import cmd
import threading
import time
import logging

from ship import Ship
from navigation import Navigation
from events import random_event

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShipCommandPrompt(cmd.Cmd):
    intro = "Welcome to Lines of Command! Type ? to list commands.\n"
    prompt = "(ship) "
    
    def __init__(self):
        super().__init__()
        self.ship = Ship()
        self.navigation = Navigation()
        self.is_sailing = False
        self.stop_event = threading.Event()
        self.event_thread = threading.Thread(target=self.handle_events, daemon=True)
        self.event_thread.start()

    def handle_events(self):
        while not self.stop_event.is_set():
            time.sleep(10)
            if not self.stop_event.is_set():
                self.trigger_event()

    def trigger_event(self):
        event = random_event()
        self.print_event(event)
        logging.info(f"Event occurred: {event}")

    def print_event(self, event):
        print(f"\n{event}\n{self.prompt}", end='')

    def do_sail(self, arg):
        """Sail the ship."""
        if self.is_sailing:
            print("The ship is already sailing.")
            logging.warning("Attempted to sail while already sailing.")
        else:
            self.is_sailing = True
            print("Sailing...")
            logging.info("Ship started sailing.")

    def do_stop(self, arg):
        """Stop the ship."""
        if not self.is_sailing:
            print("The ship is not sailing.")
            logging.warning("Attempted to stop while not sailing.")
        else:
            self.is_sailing = False
            print("Stopping the ship.")
            logging.info("Ship stopped sailing.")

    def do_turn(self, direction):
        """
        Turn the ship in the specified direction.

        Args:
            direction (str): The direction to turn the ship ('port' or 'starboard').
        """
        if direction not in ["port", "starboard"]:
            print("Invalid direction. Use 'port' or 'starboard'.")
            return
        new_direction = self.navigation.turn(direction)
        print(f"Turning {direction}. New direction: {new_direction}")
        logging.info(f"Ship turned {direction} to {new_direction}.")

    def do_status(self, arg):
        """Display the current status of the ship."""
        status = self.ship.get_status()
        print(status)
        logging.info("Displayed ship status.")

    def do_fire(self, side):
        """Fire the cannons on the specified side (port or starboard)."""
        if side not in ["port", "starboard"]:
            print("Invalid side. Use 'port' or 'starboard'.")
            return
        print(f"Firing {side} cannons!")
        logging.info(f"Fired {side} cannons.")

    def do_quit(self, arg):
        """Quit the game."""
        print("Quitting the game.")
        self.stop_event.set()  # Signal the event thread to stop
        logging.info("Game quitting.")
        return True

    def do_EOF(self, line):
        """Handle EOF to quit the game."""
        return self.do_quit(line)

    def help_turn(self):
        print("Turn the ship. Usage: turn [port|starboard]")

    def complete_turn(self, text, line, begidx, endidx):
        return [direction for direction in ['port', 'starboard'] if direction.startswith(text)]

    def complete_fire(self, text, line, begidx, endidx):
        return [side for side in ['port', 'starboard'] if side.startswith(text)]

    # Additional commands
    def do_library(self, arg):
        """Display the list of texts in the ship's library."""
        library_texts = [
            "On Naval Tactics by John Clerk of Eldin",
            "Instructions for Naval Officers (Royal Navy Manual, 1803)",
            "The Influence of Sea Power upon History, 1660-1783 by Alfred Thayer Mahan",
            "The Mariners' Compass Rectified by Andrew Wakely",
            "A New and Complete System of Navigation by John Hamilton Moore"
        ]
        print("Ship's Library:")
        for text in library_texts:
            print(f" - {text}")
        logging.info("Displayed ship's library.")

    def help_library(self):
        print("Display the list of texts in the ship's library. Usage: /library")

    def do_help(self, arg):
        """List available commands with descriptions."""
        if arg:
            # If a specific command is provided, show detailed help for that command
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                print(f"No help available for {arg}")
            else:
                func()
        else:
            # General help message listing all commands
            print("Available commands:")
            for command in self.get_names():
                if command.startswith('do_'):
                    cmd_name = command[3:]
                    cmd_func = getattr(self, command)
                    print(f"{cmd_name}: {cmd_func.__doc__}")

if __name__ == "__main__":
    ShipCommandPrompt().cmdloop()