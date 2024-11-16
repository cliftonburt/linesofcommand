officers = {
    "Captain": {
        "name": "Captain John Smith",
        "role": "Captain",
        "advice": "Maintain discipline and keep the crew motivated."
    },
    "First Mate": {
        "name": "First Mate William Turner",
        "role": "First Mate",
        "advice": "Ensure the ship's operations run smoothly."
    }
}

def get_officer_advice(role):
    officer = officers.get(role)
    if officer:
        return officer["advice"]
    else:
        return "No such officer found."

def list_officers():
    print("Officers on board:")
    for role, officer in officers.items():
        print(f"- {officer['role']}: {officer['name']}")