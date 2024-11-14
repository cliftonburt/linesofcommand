import os
import openai
from rich.console import Console
from datetime import datetime

# Initialize OpenAI API and Console
openai.api_key = os.getenv("OPENAI_API_KEY")
console = Console()

def get_chat_response(prompt, role="First Officer"):
    """
    Sends the player's prompt to OpenAI and returns a character's response.
    """
    full_prompt = (
        f"You are {role} aboard a British man-o-war in 1805. "
        f"The Captain has given the following command: '{prompt}'. "
        "Respond in character with naval jargon, confirming the order and directing the crew."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=60,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return "I'm sorry, Captain, there seems to be an issue with the command."

def chat_loop():
    """
    Main chat loop capturing player input, sending it to AI, and displaying the response.
    """
    console.print("[bold blue]Welcome aboard, Captain![/bold blue] [dim]Type 'exit' to end the session.[/dim]")
    
    chat_history = []  # Log of all messages

    while True:
        # Capture player input
        player_input = console.input("[bold green]Captain> [/bold green]")
        
        if player_input.lower() in ["quit", "exit"]:
            console.print("[bold cyan]First Officer:[/bold cyan] Aye, Captain. Ending the session.")
            break

        # Get response from the AI
        officer_response = get_chat_response(player_input)

        # Log and display messages with timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        chat_history.append((f"{timestamp} Captain", player_input))
        chat_history.append((f"{timestamp} First Officer", officer_response))
        
        # Display the chat history
        for speaker, message in chat_history[-4:]:  # Show last 4 exchanges for scrolling effect
            console.print(f"[bold cyan]{speaker}:[/bold cyan] {message}")

if __name__ == "__main__":
    chat_loop()
