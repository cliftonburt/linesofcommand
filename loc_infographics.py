from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table
from rich.text import Text

console = Console()

# Gunnery Drill Panel
def gunnery_drill():
    console.print("[bold red][Alert][/bold red]: Gunnery Drill Initiated - Objective: Achieve efficient loading and firing")
    console.print("\nCaptain> load cannons")
    console.print("First Officer: “Aye, Captain. Men are loading the cannons as ordered.”\n")

    with Progress(
        TextColumn("[bold red][Progress][/bold red]: Cannons loading...", justify="left"),
        BarColumn(bar_width=20, style="red"),
        TextColumn("[bold red]{task.percentage:>3.0f}%[/bold red]")
    ) as progress:
        loading_task = progress.add_task("loading", total=100)
        progress.update(loading_task, completed=50)  # 50% loaded
    console.print("\nCaptain> fire!")

    console.print("[bold green][Update][/bold green]: Shot completed in 87 seconds. Efficiency achieved.")
    console.print("Gunnery Officer: “Well done, Captain. The men have achieved the required speed and accuracy.”\n")

# Navigation Drill Panel
def navigation_drill():
    console.print("[bold red][Alert][/bold red]: Navigation Drill Initiated - Objective: Determine position using dead reckoning")
    console.print("\nCaptain> use sextant to locate position")
    console.print("Navigation Officer, Lt. Hardy: “Aye, Captain, sighting the horizon. Calculating latitude and longitude.”\n")

    progress_text = Text("Position determined at 40° 12’ N, 6° 5’ W.", style="bold #FF3399")
    console.print("[bold magenta][Progress][/bold magenta]: ", progress_text)
    console.print("\nCaptain> plot course based on position")

    console.print("[bold green][Update][/bold green]: Navigation drill successful. Course plotted with 95% accuracy.")
    console.print("Navigation Officer: “Captain, we are on course and heading true.”\n")

# Maintenance Log - Hull and Deck Repairs
def maintenance_log():
    console.print("[bold cyan]HMS Resolute - Maintenance Log: Hull and Deck Repairs[/bold cyan]")

    with Progress(
        TextColumn("Lower Hull Seals"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("90% (Pitching in progress)")
    ) as progress:
        progress.add_task("", total=100, completed=90)
    with Progress(
        TextColumn("Upper Deck Caulking"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("85% (Applying tar)")
    ) as progress:
        progress.add_task("", total=100, completed=85)
    # Add more tasks as seen in the visual reference above

    console.print("[bold red][Report][/bold red]: Ship repairs are nearing completion, Captain. Estimated readiness in 1 hour.\n")

# Battle Readiness - Armament Checks
def battle_readiness():
    console.print("[bold cyan]HMS Resolute - Battle Readiness: Armament Checks[/bold cyan]")

    with Progress(
        TextColumn("Cannons Loaded"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("95% (Final checks)")
    ) as progress:
        progress.add_task("", total=100, completed=95)
    with Progress(
        TextColumn("Gunpowder Reserves"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("85% (Secured)")
    ) as progress:
        progress.add_task("", total=100, completed=85)
    # Add more tasks as seen in the visual reference above

    console.print("[bold red][Update][/bold red]: Armament preparations near completion. Final officer report due in 30 minutes.\n")

# Rum Rations and Morale Update
def rum_rations_morale():
    console.print("[bold cyan]HMS Resolute - Rum Rations and Morale Update[/bold cyan]")

    with Progress(
        TextColumn("Rum Casks Opened"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("90% (Distributed)")
    ) as progress:
        progress.add_task("", total=100, completed=90)
    with Progress(
        TextColumn("Mess Area Cleanliness"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("75% (Tables cleared)")
    ) as progress:
        progress.add_task("", total=100, completed=75)
    # Add more tasks as seen in the visual reference above

    console.print("[bold magenta][Evening Report][/bold magenta]: Rum rations served. Crew morale maintained. Night duties assigned.\n")

# Deck Repair Status
def deck_repair_status():
    console.print("[bold cyan]HMS Resolute - Deck Repair Status[/bold cyan]")

    with Progress(
        TextColumn("Main Deck"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("80%")
    ) as progress:
        progress.add_task("", total=100, completed=80)
    with Progress(
        TextColumn("Gun Deck"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("70%")
    ) as progress:
        progress.add_task("", total=100, completed=70)
    # Add more tasks as seen in the visual reference above

    console.print("[bold red][Repair Progress][/bold red]: Deck repairs are underway, expected completion by dawn.\n")

# Provisions Levels
def provisions_levels():
    console.print("[bold cyan]HMS Resolute - Provisions Levels[/bold cyan]")

    with Progress(
        TextColumn("Water"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("70% - (Sufficient for 20 days)")
    ) as progress:
        progress.add_task("", total=100, completed=70)
    with Progress(
        TextColumn("Food"),
        BarColumn(bar_width=20, style="white"),
        TextColumn("90% - (Sufficient for 27 days)")
    ) as progress:
        progress.add_task("", total=100, completed=90)
    # Add more tasks as seen in the visual reference above

    console.print("[bold magenta][Captain’s Note][/bold magenta]: Resupply rum and medical provisions at next port.\n")

# Run all sections to display full dashboard
def display_dashboard():
    gunnery_drill()
    navigation_drill()
    maintenance_log()
    battle_readiness()
    rum_rations_morale()
    deck_repair_status()
    provisions_levels()

# Execute the dashboard display
display_dashboard()
