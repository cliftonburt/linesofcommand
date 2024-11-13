from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text
from rich.box import SIMPLE, ROUNDED

# Initialize the console
console = Console()

# Health and System Status Dashboard with Mixed Elements
def health_status_dashboard():
    table = Table(title="Health Status", box=SIMPLE)
    table.add_column("System", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Details", style="green")

    table.add_row("Navigation", "Operational", "All systems go")
    table.add_row("Weather", "Warning", "Storm approaching")
    table.add_row("Weapons", "Offline", "Maintenance required")

    console.print(table)

# Crew Morale with Progress Bars and Panels
def crew_morale():
    console.print("[bold #FFCC00][!] Alert: Morale is moderate; ensure sustained readiness[/]")  # Warning

# Mission Objectives with Nested Panels
def mission_objectives():
    objective_panel = Panel(
        Text("Mission: Protect Trade Route", style="bold #33FF33"),
        border_style="#FFCC00",
        style="bold #FF9933"
    )
    sub_objectives_panel = Panel(
        Text("\n".join([
            "- Intercept Hostile Vessels [bold #00FF00]Completed[/]",
            "- Safeguard Merchant Ships [#FFCC00]In Progress[/]",
            "- Maintain Supplies [#00FF00]Good Condition[/]"
        ]), style="#33FF33"),
        border_style="#33CCFF",
        title="Sub-Objectives",
        style="bold #33FF33"
    )
    console.print(objective_panel)
    console.print(sub_objectives_panel)

# Battle Readiness with Gauge and Alerts
def battle_readiness():
    console.print(Panel("Battle Readiness", style="#FF9933", border_style="#FF3333"))
    
    with Progress(
        TextColumn("[bold #FF9933]{task.description}", justify="left"),
        BarColumn(bar_width=None, style="#33FF33", complete_style="#FFCC00"),
        TextColumn("[#FFCC00]{task.percentage:>3.0f}%")
    ) as progress:
        cannon_task = progress.add_task("Cannons Loaded", total=100)
        ammunition_task = progress.add_task("Ammunition", total=100)
        morale_task = progress.add_task("Crew Morale", total=100)
        
        progress.update(cannon_task, completed=90)  # 90% cannons loaded
        progress.update(ammunition_task, completed=65)  # 65% ammunition
        progress.update(morale_task, completed=75)  # 75% morale
    
    console.print("[bold #FFCC00][!] Alert: Morale is moderate; ensure sustained readiness[/]")  # Warning

# Supply Status with Color-coded Table
def supply_status():
    table = Table(title="Supplies Overview", box=SIMPLE)
    table.add_column("Supply", justify="left", style="bold #33FF33")
    table.add_column("Status", justify="center", style="bold #FFCC00")
    table.add_column("Remaining", justify="right", style="bold #FF9933")

    table.add_row("Food", "[bold #00FF00]Ample[/]", "10 Days")
    table.add_row("Water", "[bold #FFCC00]Moderate[/]", "6 Days")
    table.add_row("Gunpowder", "[bold #FF3333]Low[/]", "2 Days")
    table.add_row("Medical Supplies", "[bold #00FF00]Sufficient[/]", "8 Days")
    
    console.print(table)

# System Diagnostic Panel with Mixed Colors
def system_diagnostics():
    diagnostic_table = Table(title="System Diagnostics", box=ROUNDED)
    diagnostic_table.add_column("System", justify="left", style="bold #33FF33")
    diagnostic_table.add_column("Status", justify="center", style="bold #FFCC00")
    diagnostic_table.add_column("Details", justify="right", style="bold #FF9933")

    diagnostic_table.add_row("Navigation", "[bold #00FF00]Operational[/]", "All systems go")
    diagnostic_table.add_row("Weather", "[bold #FFCC00]Warning[/]", "Storm approaching")
    diagnostic_table.add_row("Weapons", "[bold #FF3333]Offline[/]", "Maintenance required")

    console.print(diagnostic_table)

# Summary Dashboard
def summary_dashboard():
    console.print("[bold #FFFFFF]Lines of Command Status Summary[/]")  # Title
    health_status_dashboard()
    crew_morale()
    mission_objectives()
    battle_readiness()
    supply_status()
    system_diagnostics()

# Display summary dashboard
summary_dashboard()
