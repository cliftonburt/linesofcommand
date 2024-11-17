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
# from visuals.dashboards import refresh_dashboard

# List of all commands
COMMANDS = [
    "sail [direction] – Move the ship in a specified direction (N, S, E, W, NE, NW, SE, SW).",
    "set course [location] – Plot a course to a known destination.",
    "drop anchor – Stop the ship and hold position.",
    "weigh anchor – Prepare the ship to set sail.",
    "shorten sail – Reduce sail area to slow down.",
    "make sail – Increase sail area to pick up speed.",
    "lay by – Wait in position without moving forward.",
    "take soundings – Measure the water depth to avoid grounding.",
    "spy with glass – Use a spyglass to examine distant objects or ships.",
    "chart course – View a map of the surrounding area.",
    "high cotton – Sail at full speed with all sails aloft.",
    "engage [target] – Initiate combat with a nearby ship.",
    "fire [cannons] – Fire the ship’s cannons at a target.",
    "cease fire – Order the gunners to stop firing.",
    "double-shot – Load cannons with double shot for close-range combat.",
    "rake [target] – Fire across the length of an enemy ship for maximum damage.",
    "brace – Order the crew to brace for an incoming attack.",
    "board [ship] – Attempt to board a nearby vessel.",
    "grapple – Use grappling hooks to secure an enemy ship for boarding.",
    "strike colors – Surrender your ship to an enemy.",
    "status – View the ship’s current condition, crew morale, and resources.",
    "inspect ship – Perform a detailed inspection of the ship’s condition.",
    "repair [part] – Assign the crew to repair a damaged part of the ship.",
    "ration [amount] – Adjust the amount of food and water given to the crew.",
    "splice the mainbrace – Distribute rum to the crew to boost morale.",
    "muster the crew – Call the crew together for inspection or assignments.",
    "sound the well – Check for leaks by measuring water in the bilge.",
    "ready the longboat – Prepare the longboat for boarding or shore expeditions.",
    "pipe down – Order the crew to rest or cease activities.",
    "careen – Tilt the ship for hull maintenance.",
    "take on provisions – Resupply food, water, and rum at a port.",
    "inspect powder – Check the ship’s gunpowder stores.",
    "cargo manifest – View the current cargo and inventory.",
    "redistribute cargo – Adjust the cargo placement to balance the ship.",
    "load [item] – Add items to the ship’s cargo hold.",
    "unload [item] – Remove items from the ship’s cargo hold.",
    "trade [item] – Exchange goods with another ship or port.",
    "hail [target] – Attempt to communicate with another ship or port.",
    "decode message – Decrypt intercepted communications or signals.",
    "interrogate [spy] – Question a captured spy for intelligence.",
    "read orders – Review the most recent orders from the Admiralty.",
    "report – Send a report back to the Admiralty or receive new orders.",
    "log this – Record a notable event or discovery in the Captain’s log.",
    "decode [cipher] – Solve ciphers, such as Caesar or substitution ciphers.",
    "interpret [semaphore] – Decipher semaphore signals.",
    "calculate position – Use dead reckoning to estimate the ship’s location.",
    "diagnose [problem] – Investigate and resolve mechanical failures.",
    "identify [ship] – Use ship features to determine its origin or allegiance.",
    "search [area] – Look for clues or hidden objects in the environment.",
    "advise – Request suggestions from the officers based on the current situation.",
    "promote [crew member] – Assign or promote a crew member to a key position.",
    "discipline [crew member] – Handle unruly or underperforming crew.",
    "listen to [officer] – Hear a specific officer’s opinion on the situation.",
    "dock [port] – Enter a port to resupply or receive missions.",
    "disembark – Send a small crew ashore for specific tasks.",
    "explore – Investigate a nearby island or coastal area.",
    "salvage [wreckage] – Search the remains of a ship for useful items.",
    "search hold – Examine the ship’s cargo for contraband or needed supplies.",
    "help – View a list of available commands.",
    "save – Save the current game state.",
    "load – Load a previously saved game state.",
    "quit – Exit the game.",
    "time – Check the current in-game time and date.",
    "strike the bell – Mark the passage of time aboard the ship.",
    "name the ship – Rename your ship to something more fitting.",
    "crew list – View a roster of the ship’s crew and their statuses.",
    "write log – Add a custom entry to the ship’s logbook.",
    "fast forward – Skip uneventful travel or wait until the next significant event."
]

# Function to display help commands
def display_help():
    print("\nAvailable Commands:")
    print("\n".join(f"- {cmd}" for cmd in COMMANDS))
    print("\nType a command to proceed.\n")

# Main input loop
while True:
    user_input = input("Enter command: ").strip().lower()
    if user_input in {"/help", "help", "[9]"}:
        display_help()
    elif user_input == "quit":
        print("Goodbye, Captain!")
        break
    else:
        print("Unrecognized command. Type '/help' for a list of commands.")


def parse_command(command):
    """
    Parse the player command and execute the corresponding action.
    
    Args:
        command (str): The command input by the player.
    
    Returns:
        str: The result of the command execution.
    """
    command = command.lower()
    if command.startswith("sail"):
        direction = command.split()[1]
        return f"Sailing {direction}"
    elif command.startswith("set course"):
        location = command.split()[2]
        return f"Setting course to {location}"
    elif command == "drop anchor":
        return "Dropping anchor"
    elif command == "weigh anchor":
        return "Weighing anchor"
    elif command == "shorten sail":
        return "Shortening sail"
    else:
        return "Unknown command"

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