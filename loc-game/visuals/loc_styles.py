from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

console = Console(theme=custom_theme)

def print_info(message):
    console.print(message, style="info")

def print_warning(message):
    console.print(message, style="warning")

def print_danger(message):
    console.print(message, style="danger")