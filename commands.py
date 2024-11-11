def parse_command(command):
    """
    Parse the given command and return the action and argument.

    Args:
        command (str): The command to parse.

    Returns:
        tuple: A tuple containing the action and argument.
    """
    if command in ["move north", "move south", "move east", "move west"]:
        return "move", command.split()[1]
    else:
        return "unknown", None