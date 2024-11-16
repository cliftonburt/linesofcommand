import json
from settings import settings_manager
from game_core import achievements
from visuals import loc_styles, dashboards, maps
from missions import mission_loader
from puzzles import puzzle_engine
from npc import officers, pip

def parse_command(command, settings):
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
    elif command == "exit":
        response = "exit"
    else:
        response = f"Unknown command: {command}"
    return response