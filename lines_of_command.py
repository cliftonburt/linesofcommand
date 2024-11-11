import cmd
import threading
import time
from rich.console import Console
from rich.table import Table
from rich.progress import track
from ship import Ship
from navigation import Navigation
from events import random_event

console = Console()

class ShipCommandPrompt(cmd.Cmd):
    intro = "Welcome to Lines of Command! Type ? to list commands.\n"
    prompt = "(Captain) "
    
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
            time.sleep(1200)  # 20 minutes
            if not self.stop_event.is_set():
                self.trigger_event()

    def trigger_event(self):
        event = random_event()
        self.print_event(event)

    def print_event(self, event):
        console.print(f"\n{event}\n{self.prompt}", end='')

    def do_sail(self, arg):
        """Sail the ship."""
        if self.is_sailing:
            console.print("The ship is already sailing.", style="bold red")
        else:
            self.is_sailing = True
            console.print("Sailing...", style="bold green")

    def do_stop(self, arg):
        """Stop the ship."""
        if not self.is_sailing:
            console.print("The ship is not sailing.", style="bold red")
        else:
            self.is_sailing = False
            console.print("Stopping the ship.", style="bold green")

    def do_turn(self, direction):
        """
        Turn the ship in the specified direction.

        Args:
            direction (str): The direction to turn the ship ('port' or 'starboard').
        """
        if direction not in ["port", "starboard"]:
            console.print("Invalid direction. Use 'port' or 'starboard'.", style="bold red")
            return
        new_direction = self.navigation.turn(direction)
        console.print(f"Turning {direction}. New direction: {new_direction}", style="bold green")

    def do_status(self, arg):
        """Display the current status of the ship."""
        status = self.ship.get_status()
        console.print(status, style="bold cyan")

    def do_fire(self, side):
        """Fire the cannons on the specified side (port or starboard)."""
        if side not in ["port", "starboard"]:
            console.print("Invalid side. Use 'port' or 'starboard'.", style="bold red")
            return
        console.print(f"Firing {side} cannons!", style="bold green")

    def do_quit(self, arg):
        """Quit the game."""
        console.print("Quitting the game.", style="bold red")
        self.stop_event.set()  # Signal the event thread to stop
        return True

    def do_EOF(self, line):
        """Handle EOF to quit the game."""
        return self.do_quit(line)

    def help_turn(self):
        console.print("Turn the ship. Usage: turn [port|starboard]", style="bold cyan")

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
        table = Table(title="Ship's Library")
        table.add_column("Title", style="cyan", no_wrap=True)
        for text in library_texts:
            table.add_row(text)
        console.print(table)

    def help_library(self):
        console.print("Display the list of texts in the ship's library. Usage: /library", style="bold cyan")

    def do_help(self, arg):
        """List available commands with descriptions."""
        if arg:
            # If a specific command is provided, show detailed help for that command
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                console.print(f"No help available for {arg}", style="bold red")
            else:
                func()
        else:
            # General help message listing all commands
            console.print("Available commands:", style="bold cyan")
            for command in self.get_names():
                if command.startswith('do_'):
                    cmd_name = command[3:]
                    cmd_func = getattr(self, command)
                    console.print(f"{cmd_name}: {cmd_func.__doc__}", style="bold green")

if __name__ == "__main__":
    ShipCommandPrompt().cmdloop()