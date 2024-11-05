from map import Map
from npc import NPC
from commands import parse_command

def run_game(player):
    game_map = Map()  # Initialize a simple 5x5 map
    npcs = [NPC()]  # Create a single NPC for testing

    while player.health > 0:
        game_map.display(player, npcs)
        command = input("Enter command (move north/south/east/west): ").strip().lower()
        action, direction = parse_command(command)
        
        if action == "move":
            player.move(direction)
            
            # Check for encounters
            for npc in npcs:
                if player.position == npc.position:
                    print(f"You encountered {npc.name}!")
                    # Simple interaction or battle
                    player.health -= 10  # Simulate damage for demonstration
                    print(f"You fought {npc.name} and lost 10 health.")
                    if player.health <= 0:
                        print("You have been defeated!")
                        return  # End game if health reaches 0

        elif action == "unknown":
            print("Invalid command.")
        
        # Example victory condition
        if player.position == (4, 4):
            print("Congratulations! You've reached your objective!")
            break