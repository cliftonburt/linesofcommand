from utils.json_handler import load_json, save_json

def load_settings():
    return load_json("settings/settings.json")

def save_settings(settings):
    save_json("settings/settings.json", settings)