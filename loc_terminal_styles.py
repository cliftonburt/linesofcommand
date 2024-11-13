from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Initialize the console
console = Console()

# 1. Welcome Screen
console.print(Panel(
    "Welcome to Lines of Command",
    style="#CCFF33",  # Yellow-green for title
    border_style="#CCFF33",
))

# 2. Status Dashboard with Success and Incomplete Colors
console.print("[bold #00FF00]Navigation Status: Online[/bold #00FF00]")  # Bright green for success
console.print("[#00CC00]Combat Readiness: Incomplete[/]")        # Dark green for incomplete
supplies_text = Text("Supplies: Fully Stocked", style="bold #00FF00")
console.print(supplies_text)

# 3. Command Prompt Section with Accent Blue and Highlight Orange
console.print(Panel(
    ">>> Enter Command: Load Cannons",
    style="#33CCFF",         # Accent blue for text
    border_style="#FF9933",  # Highlight orange for border
))

# 4. Alert Panel with Warning and Error Colors
console.print("[bold #FFCC00][!] Warning: Storm Approaching[/]")    # Amber for warning
console.print("[bold #FF3333][!!!] Critical Error: Hull Damage Detected[/]")  # Red for error

# 5. Mission Briefing Layout with Dimmed Green for Subtle Sections
console.print("[bold #CCFF33]Mission Briefing[/]")  # Yellow-green for header
console.print("[#33FF33]Objective: Secure trade routes in hostile waters.[/]")  # Primary green for main objective
console.print("[#007700]Secondary Objective: Recover any lost cargo.[/]")       # Dimmed green for secondary objective

# 6. Progress Indicators in Success and Incomplete Colors
console.print("[#00CC00][####        ] 40% Incomplete[/]")  # Darker green for incomplete
console.print("[#00FF00][##########  ] 90% Complete[/]")    # Bright green for success

# 7. Navigation Map Layout with Yellow-Green and Accent Blue Borders
console.print(Panel(
    "Navigation Map Overview\n░░░░░░░░░░  ~ Current Position\n░░░░░░░░░░  ──────── Port",
    style="#33CCFF",         # Accent blue for map text
    border_style="#CCFF33",   # Yellow-green for border
))

# 8. Error Report in Error Red and Dimmed Green Text
console.print("[bold #FF3333]System Error Report[/]")          # Red for title
console.print("[#FF3333]Critical Issue: Main Mast Damaged[/]")  # Red for critical issue
console.print("[#007700]Additional Details: Inspection Required[/]")  # Dimmed green for additional info

# 9. Daily Log Entries with Title Border and Primary Text
console.print(Panel(
    "0800 Hours: Spotted enemy ship on horizon.\n1000 Hours: All crew on alert, prepared for battle.",
    style="#33FF33",         # Primary green for log text
    border_style="#CCFF33",  # Yellow-green for title and border
))

# 10. System Diagnostic with Mixed Status Colors
console.print("[bold #00FF00]Navigation Systems: Operational[/]")      # Green for operational
console.print("[bold #FFCC00]Weather Systems: Warning[/]")             # Amber for warning
console.print("[bold #FF3333]Weapon Systems: Offline[/]")              # Red for critical error

# 11. Crew Morale Tracker with Highlight Colors
console.print(Panel(
    "Status: High Spirits\nSupplies: Low - Rationing Required\nNote: Crew shows fatigue signs",
    style="#00FF00",         # Bright green for status
    border_style="#CCFF33"   # Yellow-green for panel border
))

# 12. Prompting Player Action with Accent Blue
console.print(Panel(
    ">>> Awaiting Your Command",
    style="#33CCFF",         # Accent blue for prompt text
    border_style="#33CCFF",  # Matching blue for cohesive look
))
