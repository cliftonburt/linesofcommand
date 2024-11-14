import cmd
import threading
import time
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.traceback import install
from rich.progress import Progress
from ship import Ship
from navigation import Navigation
from events import random_event

# Initialize the rich console for styled output
console = Console(force_terminal=True)

# Install rich traceback handler for better error visualization
install()

class ShipCommandPrompt(cmd.Cmd):
    """
    Command-line interface for the 'Lines of Command' game.
    
    This class provides an interactive prompt for the player to control the ship,
    navigate, engage in combat, and manage the ship's status.
    """
    
    intro = "Welcome to Lines of Command! Type ? to list commands.\n"
    prompt = "(Captain) "
    
    def __init__(self):
        """
        Initialize the ShipCommandPrompt with ship and navigation objects,
        and start the event handling thread.
        """
        super().__init__()
        self.ship = Ship()
        self.navigation = Navigation()
        self.is_sailing = False
        self.stop_event = threading.Event()
        self.event_thread = threading.Thread(target=self.handle_events, daemon=True)
        self.event_thread.start()

    def handle_events(self):
        """
        Handle periodic events in the game.
        
        This method runs in a separate thread and triggers random events every 20 minutes.
        """
        while not self.stop_event.is_set():
            time.sleep(1200)  # 20 minutes
            if not self.stop_event.is_set():
                self.trigger_event()

    def trigger_event(self):
        """
        Trigger a random event and print it to the console.
        """
        event = random_event()
        self.print_event(event)

    def print_event(self, event):
        """
        Print the event message to the console.
        
        Args:
            event (str): The event message to print.
        """
        console.print(f"\n{event}\n{self.prompt}", end='')

    def do_sail(self, arg):
        """
        Sail the ship.
        
        This command starts the ship sailing if it is not already sailing.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        if self.is_sailing:
            console.print("[bold red]The ship is already sailing.[/bold red]")
        else:
            self.is_sailing = True
            console.print("[bold green]Sailing...[/bold green]")

    def do_stop(self, arg):
        """
        Stop the ship.
        
        This command stops the ship if it is currently sailing.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        if not self.is_sailing:
            console.print("[bold red]The ship is not sailing.[/bold red]")
        else:
            self.is_sailing = False
            console.print("[bold green]Stopping the ship.[/bold green]")

    def do_turn(self, direction):
        """
        Turn the ship in the specified direction.
        
        Args:
            direction (str): The direction to turn the ship ('port' or 'starboard').
        """
        if direction not in ["port", "starboard"]:
            console.print("[bold red]Invalid direction. Use 'port' or 'starboard'.[/bold red]")
            return
        new_direction = self.navigation.turn(direction)
        console.print(f"Turning {direction}. New direction: {new_direction}", style="bold green")

    def do_status(self, arg):
        """
        Display the current status of the ship.
        
        This command retrieves and displays the ship's status and specifications in a table format.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        try:
            status = self.ship.get_status()
            specs = self.ship.get_specs()
            
            table = Table(title="Ship Status and Specifications", show_header=True, header_style="bold magenta")
            table.add_column("Attribute", style="cyan", no_wrap=True)
            table.add_column("Value", style="magenta", justify="left", overflow="fold")
            
            for key, value in specs.items():
                table.add_row(key, str(value))
            
            table.add_row("----", "----")
            
            for key, value in status.items():
                table.add_row(key, str(value))
            
            console.print(table)
        except AttributeError as e:
            console.print(f"[bold red]Error: Ship object has no attribute 'get_status' or 'get_specs'.[/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Unexpected error: {e}[/bold red]")

    def do_fire(self, side):
        """
        Fire the cannons on the specified side.
        
        Args:
            side (str): The side to fire the cannons ('port' or 'starboard').
        """
        if side not in ["port", "starboard"]:
            console.print("[bold red]Invalid side. Use 'port' or 'starboard'.[/bold red]")
            return
        console.print(f"Firing {side} cannons!", style="bold green")

    def do_quit(self, arg):
        """
        Quit the game.
        
        This command stops the event handling thread and exits the game.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        console.print("[bold red]Quitting the game.[/bold red]")
        self.stop_event.set()  # Signal the event thread to stop
        return True

    def do_EOF(self, line):
        """
        Handle EOF to quit the game.
        
        This command is triggered when the user presses Ctrl+D.
        
        Args:
            line (str): The input line (not used).
        """
        return self.do_quit(line)

    def help_turn(self):
        """
        Display help for the 'turn' command.
        """
        console.print("Turn the ship. Usage: turn [port|starboard]", style="bold cyan")

    def complete_turn(self, text, line, begidx, endidx):
        """
        Provide tab completion for the 'turn' command.
        
        Args:
            text (str): The current text being typed.
            line (str): The entire input line.
            begidx (int): The beginning index of the text being completed.
            endidx (int): The ending index of the text being completed.
        
        Returns:
            list: A list of possible completions.
        """
        return [direction for direction in ['port', 'starboard'] if direction.startswith(text)]

    def complete_fire(self, text, line, begidx, endidx):
        """
        Provide tab completion for the 'fire' command.
        
        Args:
            text (str): The current text being typed.
            line (str): The entire input line.
            begidx (int): The beginning index of the text being completed.
            endidx (int): The ending index of the text being completed.
        
        Returns:
            list: A list of possible completions.
        """
        return [side for side in ['port', 'starboard'] if side.startswith(text)]

    # Additional commands
    def do_library(self, arg):
        """
        Display the list of texts in the ship's library.
        
        Args:
            arg (str): Additional arguments (not used).
        """
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
        """
        Display help for the 'library' command.
        """
        console.print("Display the list of texts in the ship's library. Usage: /library", style="bold cyan")

    def do_read_manual(self, arg):
        """
        Read the ship's manual.
        
        This command displays the ship's manual in Markdown format.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        manual_content = """
        # Ship's Manual
        ## Navigation
        - Use `turn port` to turn the ship to the left.
        - Use `turn starboard` to turn the ship to the right.
        ## Combat
        - Use `fire port` to fire the cannons on the left side.
        - Use `fire starboard` to fire the cannons on the right side.
        """
        markdown = Markdown(manual_content)
        console.print(markdown)

    def do_show_code(self, arg):
        """
        Show the source code of this script.
        
        This command displays the source code of the current script with syntax highlighting.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        try:
            with open(__file__, "r") as f:
                code = f.read()
            syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
            console.print(syntax)
        except Exception as e:
            console.print(f"Error reading source code: {e}", style="bold red")

    def do_error(self, arg):
        """
        Trigger an error to demonstrate rich tracebacks.
        
        This command raises a ValueError to demonstrate the rich traceback handler.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        raise ValueError("This is a demonstration error.")

    def do_long_task(self, arg):
        """
        Simulate a long-running task with a loading bar.
        
        Args:
            arg (str): Additional arguments (not used).
        """
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=100)
            for i in range(100):
                time.sleep(0.1)  # Simulate work being done
                progress.update(task, advance=1)
        console.print("[bold green]Task completed![/bold green]")

def do_help(self, arg):
    """
    List available commands with descriptions.

    This command displays a list of all available commands and their descriptions.

    Args:
        arg (str): The command to display detailed help for (optional).
    """
    if arg:
        # If a specific command is provided, show detailed help for that command
        try:
            func = getattr(self, 'help_' + arg)
        except AttributeError:
            console.print(f"No help available for {arg}", style="bold red")
        else:
            func()
    else:
        # Import the box module from rich for ASCII borders
        from rich import box

        # General help message listing all commands in a table with ASCII borders
        table = Table(
            title="Available Commands",
            show_header=True,
            header_style="bold magenta",
            border_style="bold blue",
            box=box.ASCII  # Use ASCII characters for table borders
        )
        table.add_column("Command", style="bold cyan", no_wrap=True)
        table.add_column("Description", style="bold magenta", justify="left", overflow="fold")

        # Collect commands and their descriptions
        commands = []
        for command in self.get_names():
            if command.startswith('do_'):
                cmd_name = command[3:]
                cmd_func = getattr(self, command)
                doc = cmd_func.__doc__
                if doc:
                    first_line = doc.strip().split('\n')[0]
                else:
                    first_line = "No description available"
                commands.append((cmd_name, first_line))

        # Sort commands alphabetically
        commands.sort()

        # Add commands to the table
        for cmd_name, description in commands:
            table.add_row(f"[bold cyan]{cmd_name}[/bold cyan]", description)

        # Print the table to the console
        console.print(table)

if __name__ == "__main__":
    ShipCommandPrompt().cmdloop()