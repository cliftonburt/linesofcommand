class Ship:
    def __init__(self):
        self.hull_integrity = 100
        self.provisions = 100
        self.position = (0, 0)
        self.name = "HMS Victory"
        self.type = "Ship of the Line"
        self.guns = 104
        self.crew = 850

    def get_status(self):
        """
        Return the current status of the ship as a dictionary.
        """
        return {
            "Hull Integrity": self.hull_integrity,
            "Provisions": self.provisions,
            "Position": self.position
        }

    def get_specs(self):
        """
        Return the specifications of the ship as a dictionary.
        """
        return {
            "Name": self.name,
            "Type": self.type,
            "Guns": self.guns,
            "Crew": self.crew
        }