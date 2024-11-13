# loc_dashboard.py

from loc_styles import console, create_color_table

def health_status_dashboard():
    table = create_color_table()
    table.title = "Health Status"
    table.add_column("System", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Details", style="green")

    table.add_row("Navigation", "Operational", "All systems go")
    table.add_row("Weather", "Warning", "Storm approaching")
    table.add_row("Weapons", "Offline", "Maintenance required")

    console.print(table)

def summary_dashboard():
    console.print("[bold #FFFFFF]Lines of Command Status Summary[/]")  # Title
    health_status_dashboard()
    # Add calls to other dashboard functions here

# Display summary dashboard
summary_dashboard()