import unittest
from unittest.mock import patch
from game_core import command_parser
from settings import settings_manager

class TestCommandParser(unittest.TestCase):

    def setUp(self):
        self.settings = settings_manager.load_settings()

    @patch('builtins.print')
    def test_help_command(self, mock_print):
        command_parser.parse_command("help", self.settings)
        mock_print.assert_any_call("Available commands: help, exit, settings, set, achievements, add_achievement, dashboard, map, missions, mission, puzzles, puzzle, officers, advice, pip")

    @patch('builtins.print')
    def test_set_command(self, mock_print):
        command_parser.parse_command("set volume 75", self.settings)
        self.assertEqual(self.settings["volume"], 75)
        mock_print.assert_any_call("Setting 'volume' updated to 75")

    @patch('builtins.print')
    def test_unknown_command(self, mock_print):
        command_parser.parse_command("unknown", self.settings)
        mock_print.assert_any_call("Unknown command: unknown")

if __name__ == "__main__":
    unittest.main()