"""
Lines of Command - Game Core System

Overview:
This file contains the core mechanics for 'Lines of Command,' an interactive fiction game set in 1805 during the Napoleonic Wars. Players command a British naval ship via a command-line interface, issuing orders related to navigation, combat, and crew management. 

Objectives:
1. Implement the command parsing system.
2. Develop the navigation and interaction mechanics for players.
3. Create basic interactions with officers who provide real-time feedback and suggestions.
4. Set up a system for handling weekly puzzles and gradually escalating complexity.

High-Level Goals for Copilot:
- Generate efficient NLP-based command parsing to understand player inputs in natural language.
- Help construct a coordinate-based navigation system where players can explore an ocean map.
- Generate methods for handling player commands like 'sail', 'engage enemy', and 'drop anchor.'
- Enable officer feedback that translates player input into historically accurate orders.

When in doubt, ask for:
- Specific edge cases that should be accounted for.
- Clarification on how a command should function or be expanded.
- Whether a feature needs to align closely with historical accuracy or be simplified for gameplay.
"""

import json
from settings import settings_manager
from game_core import achievements
from visuals import loc_styles, dashboards, maps
from missions import mission_loader
from puzzles import puzzle_engine
from npc import officers, pip
from game_core.achievements import add_achievement
#from visuals.dashboards import refresh_dashboard

VALID_COMMANDS = {
    "hoist sails": "Increases ship speed",
    "fire cannons": "Attacks nearby enemy ships",
    "check provisions": "Displays current provisions and supplies",
    "dashboard": "Shows the system dashboard",
    "exit": "Ends the game"
}

def parse_command(command: str, settings: dict):
    """
    Parses the player's command and routes it to the appropriate function.

    Args:
        command (str): The input command from the player.
        settings (dict): The current game settings.

    Returns:
        str: Status or action result, or "exit" to quit the game.
    """
    command = command.lower()
    response = ""
    if command in VALID_COMMANDS:
        if command == "hoist sails":
            response = "The crew scrambles to hoist the sails!"
            update_dashboard("speed", +1) # type: ignore
        elif command == "fire cannons":
            response = "Firing cannons at nearby enemy ships!"
            # Add logic to handle firing cannons
        elif command == "check provisions":
            response = "Current provisions and supplies: ..."
            # Add logic to display provisions
        elif command == "dashboard":
            dashboards.show_dashboard()
        elif command == "exit":
            return "exit"
    else:
        response = f"Invalid command: '{command}'. Type 'help' for a list of commands."

    return response

def parse_command_legacy(command, settings):
    response = ""
    if command == "help":
        response = "Available commands: help, exit, settings, set, achievements, add_achievement, dashboard, map, missions, mission, puzzles, puzzle, officers, advice, pip"
    elif command == "settings":
        response = json.dumps(settings, indent=4)
    elif command.startswith("set "):
        try:
            _, key, value = command.split(" ", 2)
            if key in settings:
                settings[key] = type(settings[key])(value)
                settings_manager.save_settings(settings)
                response = f"Setting '{key}' updated to {value}"
            else:
                response = f"Unknown setting: {key}"
        except ValueError:
            response = "Usage: set <setting> <value>"
    elif command == "achievements":
        response = "\n".join(achievements.list_achievements())
    elif command.startswith("add_achievement "):
        _, name = command.split(" ", 1)
        achievements.add_achievement(name)
        response = f"Achievement '{name}' added."
    elif command == "dashboard":
        dashboards.show_dashboard()
    elif command == "map":
        response = maps.generate_map()
    elif command == "missions":
        response = "\n".join(mission_loader.list_missions())
    elif command.startswith("mission "):
        try:
            _, mission_id = command.split(" ", 1)
            mission = mission_loader.get_mission_details(int(mission_id))
            if mission:
                response = f"Mission {mission_id}: {mission['name']}\n{mission['description']}"
            else:
                response = f"No mission found with ID {mission_id}"
        except ValueError:
            response = "Usage: mission <mission_id>"
    elif command == "puzzles":
        response = "\n".join(puzzle_engine.list_puzzles())
    elif command.startswith("puzzle "):
        try:
            _, puzzle_id = command.split(" ", 1)
            puzzle = puzzle_engine.get_puzzle_details(int(puzzle_id))
            if puzzle:
                response = f"Puzzle {puzzle_id}: {puzzle['name']}\n{puzzle['description']}"
            else:
                response = f"No puzzle found with ID {puzzle_id}"
        except ValueError:
            response = "Usage: puzzle <puzzle_id>"
    elif command == "officers":
        response = "\n".join(officers.list_officers())
    elif command.startswith("advice "):
        try:
            _, role = command.split(" ", 1)
            advice = officers.get_officer_advice(role)
            response = f"Advice from {role}: {advice}"
        except ValueError:
            response = "Usage: advice <officer_role>"
    elif command == "pip":
        response = pip.get_pip_action()
    else:
        response = f"Unknown command: {command}"
    return response

class CommandProcessor:
    def __init__(self):
        self.commands = {
            "semaphore": self.semaphore_signal_puzzle,
            "knot": self.knot_tying_logic,
            "navigation": self.real_time_navigation
        }

    def process_command(self, command):
        # Split the command into keywords
        keywords = command.lower().split()
        
        # Check for known commands
        for keyword in keywords:
            if keyword in self.commands:
                return self.commands[keyword]()
        
        return "Unknown command. Please try again."

    def semaphore_signal_puzzle(self):
        # Placeholder for semaphore signal puzzle logic
        return "Semaphore Signal Puzzle: [Logic to be implemented]"

    def knot_tying_logic(self):
        # Placeholder for knot-tying logic
        return "Knot-Tying Logic: [Logic to be implemented]"

    def real_time_navigation(self):
        # Placeholder for real-time navigation logic
        return "Real-Time Navigation: [Logic to be implemented]"

# Example usage
processor = CommandProcessor()
print(processor.process_command("semaphore"))
print(processor.process_command("knot"))
print(processor.process_command("navigation"))
print(processor.process_command("unknown"))