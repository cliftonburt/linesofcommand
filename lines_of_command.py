import cmd
import threading
import time
from ship import Ship
from navigation import Navigation
from events import random_event

class ShipCommandPrompt(cmd.Cmd):
    intro = "Welcome to Lines of Command! Type ? to list commands.\n"
    prompt = "(ship) "
    
    def __init__(self):
        super().__init__()
        self.ship = Ship()
        self.navigation = Navigation()
        self.event_thread = threading.Thread(target=self.handle_events, daemon=True)
        self.event_thread.start()

    def handle_events(self):
        while True:
            time.sleep(10)
            event = random_event()
            print(f"\n{event}\n{self.prompt}", end='')

    def do_sail(self, arg):
        print("Sailing...")

    def do_turn(self, direction):
        new_direction = self.navigation.turn(direction)
        print(f"Turning {direction}. New direction: {new_direction}")

    def do_status(self, arg):
        status = self.ship.get_status()
        print(status)

    def do_fire(self, side):
        print(f"Firing {side} cannons!")

    def do_quit(self, arg):
        print("Quitting the game.")
        return True

    def do_EOF(self, line):
        return self.do_quit(line)

    def help_turn(self):
        print("Turn the ship. Usage: turn [port|starboard]")

    def complete_turn(self, text, line, begidx, endidx):
        return [direction for direction in ['port', 'starboard'] if direction.startswith(text)]

    # Additional commands
    def do_library(self, arg):
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

    def help_library(self):
        print("Display the list of texts in the ship's library. Usage: /library")

if __name__ == "__main__":
    ShipCommandPrompt().cmdloop()