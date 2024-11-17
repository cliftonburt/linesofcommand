import json
from game_core.command_parser import parse_command
from settings.settings_manager import load_settings, save_settings
from visuals.dashboards import show_dashboard
from rich.console import Console
from rich.prompt import Prompt
from settings import settings_menu  # Import the settings menu

console = Console()

def display_help():
    """Displays help commands."""
    console.print("\n[bold green]Available Commands:[/bold green]")
    commands = [
        "[bold cyan]settings[/bold cyan]: Open the settings menu",
        "[bold cyan][11] settings[/bold cyan]: Open the settings menu",
        "[bold cyan]save[/bold cyan]: Save your progress",
        "[bold cyan]quit[/bold cyan]: Exit the game",
    ]
    for command in commands:
        console.print(f" - {command}")
    console.print("\n")

def main():
    """
    Main entry point for Lines of Command. Initializes settings, loads dashboards,
    and begins the gameplay loop.
    """
    console.print("[bold cyan]Welcome to Lines of Command: HMS Resolute[/bold cyan]")
    console.print("\nType [bold cyan]help[/bold cyan] for a list of commands.\n")
    
    # Load game settings
    settings = load_settings()
    
    # Show the initial dashboard
    show_dashboard()

    # Main game loop
    while True:
        user_input = Prompt.ask("$", default="help")
        console.print(f"[bold yellow]Received command: {user_input}[/bold yellow]")  # Debug print
        if user_input == "help":
            display_help()
        elif user_input == "settings" or user_input == "[11]":
            console.print("[bold green]Opening settings menu...[/bold green]")  # Debug print
            settings_menu()
        elif user_input == "save":
            save_settings(settings)
            console.print("[bold green]Progress saved.[/bold green]")
        elif user_input == "quit":
            console.print("[bold red]Goodbye, Captain![/bold red]")
            break
        else:
            result = parse_command(user_input)
            console.print(result)

if __name__ == "__main__":
    main()

