pip_actions = [
    "Pip is cleaning the deck.",
    "Pip is assisting the cook.",
    "Pip is practicing knots."
]

def get_pip_action():
    import random
    return random.choice(pip_actions)