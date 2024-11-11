# This file will contain the Ship class and logic related to the ship’s status and provisions.
class Ship:
    def __init__(self):
        self.hull_integrity = 100
        self.provisions = 100
        self.position = (0, 0)

    def get_status(self):
        return (f"Hull Integrity: {self.hull_integrity}\n"
                f"Provisions: {self.provisions}\n"
                f"Position: {self.position}")