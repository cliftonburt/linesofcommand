import json
from utils.json_handler import load_json

def load_puzzles():
    return load_json("puzzles/puzzles.json")

def get_puzzle_details(puzzle_id):
    puzzles = load_puzzles()
    for puzzle in puzzles:
        if puzzle["id"] == puzzle_id:
            return puzzle
    return None

def list_puzzles():
    puzzles = load_puzzles()
    if puzzles:
        print("Available Puzzles:")
        for puzzle in puzzles:
            print(f"- {puzzle['id']}: {puzzle['name']}")
    else:
        print("No puzzles available.")