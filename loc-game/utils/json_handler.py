import json

def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)