from settings import settings_manager
from game_core import command_parser

def main():
    print("Welcome to Lines of Command: HMS Resolute")
    settings = settings_manager.load_settings()
    while True:
        command = input("> ")
        if command.lower() in ["exit", "quit"]:
            break
        command_parser.parse_command(command, settings)

if __name__ == "__main__":
    main()