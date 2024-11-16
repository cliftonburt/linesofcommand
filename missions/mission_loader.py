import json
from utils.json_handler import load_json

def load_missions():
    return load_json("missions/mission_data.json")

def get_mission_details(mission_id):
    missions = load_missions()
    for mission in missions:
        if mission["id"] == mission_id:
            return mission
    return None

def list_missions():
    missions = load_missions()
    if missions:
        print("Available Missions:")
        for mission in missions:
            print(f"- {mission['id']}: {mission['name']}")
    else:
        print("No missions available.")