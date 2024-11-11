#This file will contain the Navigation class to handle navigation commands.
class Navigation:
    def __init__(self):
        self.direction = "north"

    def turn(self, direction):
        if direction == "port":
            self.direction = "west" if self.direction == "north" else "south" if self.direction == "west" else "east" if self.direction == "south" else "north"
        elif direction == "starboard":
            self.direction = "east" if self.direction == "north" else "south" if self.direction == "east" else "west" if self.direction == "south" else "north"
        return self.direction