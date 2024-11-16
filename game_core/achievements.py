achievements = []

def add_achievement(name):
    if name not in achievements:
        achievements.append(name)
        print(f"Achievement unlocked: {name}")

def list_achievements():
    if achievements:
        print("Achievements:")
        for achievement in achievements:
            print(f"- {achievement}")
    else:
        print("No achievements yet.")