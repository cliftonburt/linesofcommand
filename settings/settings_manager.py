import json
import os

DEFAULT_SETTINGS = {
    "color_palette": "Color",  # Options: Color, Monochrome, Green
    "sound_effects": False,
    "background_music": False,
    "kid_safe_mode": False,
    "difficulty": "Normal",  # Options: Easy, Normal, Hard
    "autosave_slot": True
}

SETTINGS_FILE = "settings.json"

def load_settings() -> dict:
    """
    Loads game settings from a JSON file.

    Returns:
        dict: The current settings or default settings if the file doesn't exist.
    """
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error loading settings. Using default settings.")
    return DEFAULT_SETTINGS

def save_settings(settings: dict):
    """
    Saves game settings to a JSON file.

    Args:
        settings (dict): The settings to save.
    """
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)