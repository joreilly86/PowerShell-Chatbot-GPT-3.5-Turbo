import os

import pyperclip  # For clipboard support
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please add it to your .env file.")

# Instantiate the OpenAI client
client = OpenAI(api_key=api_key)


def run_chatbot():
    """Runs the chatbot with streaming responses."""
    print("Chatbot is ready. Type 'exit' or 'quit' to end the session.\n")

    # Define custom instructions for the bot
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant for a professional civil engineer. "
                "Follow best practices in technical communication. Provide answers "
                "that are succinct, clear, and focused, avoiding unnecessary details or verbosity. "
                "Prioritize professionalism and accuracy in all responses."
            ),
        }
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Add the user's input to the conversation history
        messages.append({"role": "user", "content": user_input})

        try:
            # Stream responses from OpenAI
            stream = client.chat.completions.create(
                model="gpt-4o",  # Default to "gpt-4o" or "gpt-4"
                messages=messages,
                stream=True,  # Enable streaming for real-time responses
            )
            print("AI: ", end="", flush=True)
            response_content = ""

            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="", flush=True)
                    response_content += content

            print()  # Add a newline after the full response

            # Add the assistant's response to the conversation history
            messages.append({"role": "assistant", "content": response_content})

            # Copy the response to the clipboard
            pyperclip.copy(response_content)

        except Exception as e:
            print(f"An error occurred: {e}. Please check your API key or connection.")


if __name__ == "__main__":
    run_chatbot()
