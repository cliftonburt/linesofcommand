class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.health = 100
        self.position = (0, 0)  # Starting position on the map

    def move(self, direction):
        x, y = self.position
        if direction == "north":
            self.position = (x, y + 1)
        elif direction == "south":
            self.position = (x, y - 1)
        elif direction == "east":
            self.position = (x + 1, y)
        elif direction == "west":
            self.position = (x - 1, y)