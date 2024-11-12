import openai
import os

# Set your OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("No API key found in environment variables.")
else:
    openai.api_key = api_key
    print("API key successfully set.")

def interpret_command(player_input):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"You are a text-based adventure game set in the year 1805, where the player is a British naval captain. The game aims to maintain realism and historical accuracy, with terminology, responses, and actions reflecting the language and technology of the era. Interpret this command in that historical context: {player_input}",
            max_tokens=50
        )
        print(f"API response: {response}")  # Log the entire response
        if 'choices' in response and len(response['choices']) > 0:
            interpreted_command = response['choices'][0]['text'].strip()
            print(f"Interpreted command: {interpreted_command}")  # Log the interpreted command
            return interpreted_command
        else:
            print("No choices found in the response.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    player_input = "Set sail towards the enemy fleet."
    result = interpret_command(player_input)
    print(f"Result: {result}")