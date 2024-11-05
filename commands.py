def parse_command(command):
    if command in ["move north", "move south", "move east", "move west"]:
        return "move", command.split()[1]
    else:
        return "unknown", None