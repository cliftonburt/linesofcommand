class Ship:
    def __init__(self):
        self.hull_integrity = 100
        self.provisions = 100
        self.position = (0, 0)

    def get_status(self):
        """
        Return the current status of the ship as a dictionary.
        """
        return {
            "Hull Integrity": self.hull_integrity,
            "Provisions": self.provisions,
            "Position": self.position
        }