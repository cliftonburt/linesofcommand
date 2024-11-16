from visuals.loc_styles import console

def show_dashboard():
    console.print("=== HMS Resolute Dashboard ===", style="bold")
    console.print("Crew: 150", style="info")
    console.print("Cannons: 74", style="info")
    console.print("Supplies: 3 months", style="info")
    console.print("Current Mission: None", style="info")