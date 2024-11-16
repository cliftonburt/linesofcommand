import unittest
from missions import mission_loader

class TestMissionLoader(unittest.TestCase):

    def test_load_missions(self):
        missions = mission_loader.load_missions()
        self.assertIsInstance(missions, list)

    def test_get_mission_details(self):
        mission = mission_loader.get_mission_details(1)
        self.assertIsNotNone(mission)
        self.assertEqual(mission["id"], 1)

if __name__ == "__main__":
    unittest.main()