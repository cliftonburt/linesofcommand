#generate random events for the player to encounter
import random

def random_event():
    events = [
        "A storm approaches.",
        "Enemy ship sighted.",
        "Crew morale is high.",
        "Supplies are running low.",
        "The sea is calm."
    ]
    return random.choice(events)