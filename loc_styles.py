# loc_styles.py

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

# Define the color palette
COLORS = {
    "Background": "#000000",
    "Title / Border": "#CCFF33",
    "Primary Text": "#33FF33",
    "Success Status": "#00FF00",
    "Incomplete Status": "#00CC00",
    "Dimmed Green": "#007700",
    "Warning Status": "#FFCC00",
    "Error Status": "#FF3333",
    "Accent Blue": "#33CCFF",
    "Highlight Orange": "#FF9933",
    "White": "#FFFFFF"
}

# Define block elements
LIGHT_SHADE = "\u2591"  # ░
MEDIUM_SHADE = "\u2592"  # ▒
DARK_SHADE = "\u2593"  # ▓

# Initialize the console
console = Console()

def create_panel(content, title, style, border_style):
    """Create a panel with the given content, title, style, and border style."""
    return Panel(content, title=title, style=style, border_style=border_style)

def create_color_table():
    """Create a table to display all colors with their descriptions."""
    table = Table(title="CRT-Inspired Color Palette", box=box.ROUNDED)
    table.add_column("Color Name", style="bold")
    table.add_column("Hex Code", style="bold")
    table.add_column("Description", style="bold")

    descriptions = [
        "A pure black background for a classic CRT look.",
        "Yellow-green for high-contrast headers and section borders.",
        "Medium green for main text, readable on black.",
        "Bright neon green for successful actions or completed tasks.",
        "Darker green for incomplete or low-priority items.",
        "Dark green for subtle text or inactive indicators.",
        "Amber-yellow for warnings or alerts.",
        "Vivid red to indicate critical issues or errors.",
        "Light blue for accents or secondary highlights.",
        "Soft orange for key details.",
        "Bright white for main headers or critical information."
    ]

    for (name, hex_value), description in zip(COLORS.items(), descriptions):
        table.add_row(
            Text(name, style=hex_value),
            Text(hex_value, style=hex_value),
            Text(description, style=hex_value)
        )

    return table

def display_color_panels():
    """Display individual panels for each color in the palette."""
    for name, hex_value in COLORS.items():
        panel = create_panel(f"{name}\n{hex_value}", name, hex_value, hex_value)
        console.print(panel)

def display_color_table():
    """Display the color table."""
    table = create_color_table()
    console.print(table)

def display_text_styles():
    """Demonstrate text styles and borders."""
    console.print(Text("Bold Text Example", style="bold #FF3333"))

def display_final_panel():
    """Create and display a final example panel."""
    final_panel = create_panel(
        Text("Retro High-Contrast Look", style="bold #FFFFFF"),
        "Final Example",
        "bold #33CCFF",
        "bold #FF9933"
    )
    console.print(final_panel)

def display_alert_messages():
    """Display dynamic, color-coded alert messages."""
    console.print(Panel("[!] Caution: Low Wind Detected 🌊", style="bold #FFCC00", border_style="bold #FFCC00"))
    console.print(Panel("[!!!] Alert: Enemy Ships Sighted 🚢", style="bold #FF3333", border_style="bold #FF3333"))

def display_command_prompt():
    """Display an example of an interactive command prompt."""
    console.print(Panel("Enter Command: ⚓", style="bold #33CCFF", border_style="bold #33CCFF"))

def display_block_elements():
    """Display block elements in each color from the palette."""
    for name, hex_value in COLORS.items():
        block_display = f"{LIGHT_SHADE} {MEDIUM_SHADE} {DARK_SHADE}"
        panel = create_panel(block_display, name, hex_value, hex_value)
        console.print(panel)