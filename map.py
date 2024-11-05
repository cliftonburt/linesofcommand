class Map:
    def __init__(self, size=(5, 5)):
        self.size = size
        self.grid = [["." for _ in range(size[0])] for _ in range(size[1])]

    def display(self, player, npcs):
        for y in range(self.size[1]):
            row = ""
            for x in range(self.size[0]):
                if (x, y) == player.position:
                    row += "P "  # Player position
                elif any(npc.position == (x, y) for npc in npcs):
                    row += "N "  # NPC position
                else:
                    row += ". "
            print(row)
        print("\n")