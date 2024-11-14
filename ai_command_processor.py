import os
import openai
from openai.error import OpenAIError, RateLimitError
import time
from rich.console import Console
from rich.prompt import Prompt

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize console for output
console = Console()

def get_ai_response(prompt: str) -> str:
    """
    Sends the player's input as a prompt to OpenAI and returns the AI's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are the First Officer on a British man-o-war in 1805."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except RateLimitError as e:
        console.print(f"[bold red]Rate limit exceeded. Retrying...[/bold red]")
        time.sleep(5)  # Simple backoff strategy
        return get_ai_response(prompt)
    except OpenAIError as e:
        console.print(f"[bold red]OpenAI API Error:[/bold red] {e}")
        return "I'm sorry, Captain, there seems to be an issue with the command."
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
        return "I'm sorry, Captain, there seems to be an issue with the command."

def interpret_command():
    while True:
        player_input = input("Captain> ")
        if player_input.lower() in ['exit', 'quit']:
            break
        response = get_ai_response(player_input)
        print(response)

if __name__ == "__main__":
    console.print("Welcome aboard, Captain! Awaiting your command.")
    interpret_command()