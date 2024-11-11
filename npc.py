class NPC:
    def __init__(self, name="Soldier", position=(2, 2), health=50, npc_type="enemy", strength=10, dialogue=None):
        self.name = name
        self.position = position
        self.health = health
        self.npc_type = npc_type
        self.strength = strength
        self.dialogue = dialogue if dialogue is not None else []

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

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        if self.health > 50:  # Assuming 50 is the max health
            self.health = 50

    def attack(self, target):
        if isinstance(target, NPC):
            target.take_damage(self.strength)
            print(f"{self.name} attacks {target.name} for {self.strength} damage!")

    def talk(self):
        if self.dialogue:
            print(f"{self.name} says: {self.dialogue[0]}")
            self.dialogue = self.dialogue[1:] + [self.dialogue[0]]  # Rotate dialogue

    def __str__(self):
        return (f"NPC(name={self.name}, position={self.position}, health={self.health}, "
                f"npc_type={self.npc_type}, strength={self.strength})")

# Example usage
if __name__ == "__main__":
    npc = NPC(name="Guard", position=(3, 3), dialogue=["Hello, traveler!", "Stay out of trouble."])
    print(npc)
    npc.move("north")
    print(npc)
    npc.talk()
    npc.take_damage(20)
    print(npc)
    npc.heal(10)
    print(npc)
    npc.attack(NPC(name="Bandit", position=(4, 4)))