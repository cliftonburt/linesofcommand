import json
from game_core.command_parser import parse_command
from settings.settings_manager import load_settings, save_settings
from visuals.dashboards import show_dashboard

def main():
    """
    Main entry point for Lines of Command. Initializes settings, loads dashboards,
    and begins the gameplay loop.
    """
    print("Welcome to Lines of Command: HMS Resolute")
    
    # Load game settings
    settings = load_settings()
    
    # Show the initial dashboard
    show_dashboard()

    # Main game loop
    while True:
        try:
            # Get player command
            command = input("\nEnter your command: ").strip()
            # Process the command
            result = parse_command(command, settings)
            if result == "exit":
                break
        except KeyboardInterrupt:
            print("\nGoodbye, Captain!")
            break

    # Save settings before exit
    save_settings(settings)

if __name__ == "__main__":
    main()