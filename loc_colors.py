from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

# Define the color palette
colors = {
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

# Initialize the console
console = Console()

# Define block elements
light_shade = "\u2591"  # ░
medium_shade = "\u2592"  # ▒
dark_shade = "\u2593"  # ▓

# Create a display for each block element in each color
for name, hex_value in colors.items():
    block_display = f"{light_shade} {medium_shade} {dark_shade}"
    panel = Panel(block_display, title=name, style=hex_value, border_style=hex_value)
    console.print(panel)

# Create a table to display all colors
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

for (name, hex_value), description in zip(colors.items(), descriptions):
    table.add_row(
        Text(name, style=hex_value),
        Text(hex_value, style=hex_value),
        Text(description, style=hex_value)
    )

console.print(table)

# Demonstrate text styles and borders
console.print(Text("Bold Text Example", style="bold #FF3333"))

# Create a final example panel
final_panel = Panel(
    Text("Retro High-Contrast Look", style="bold #FFFFFF"),
    style="bold #33CCFF",
    border_style="bold #FF9933"
)
console.print(final_panel)

# Example of dynamic, color-coded alert messages
console.print(Panel("[!] Caution: Low Wind Detected", style="bold #FFCC00", border_style="bold #FFCC00"))
console.print(Panel("[!!!] Alert: Enemy Ships Sighted", style="bold #FF3333", border_style="bold #FF3333"))

# Example of interactive command prompt
console.print(Panel("Enter Command: ", style="bold #33CCFF", border_style="bold #33CCFF"))