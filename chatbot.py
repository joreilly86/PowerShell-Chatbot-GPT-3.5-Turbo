import openai
import pyperclip

def chat():
    """
    This function initiates a chat session using OpenAI's GPT model.

    It repeatedly prompts the user for input, sends this input to the OpenAI API,
    and prints the AI's response. The AI's response is also copied to the clipboard.
    
    To end the chat session, the user can type 'exit' or 'quit'.
    
    Requires:
    - An OpenAI API key set in the openai.api_key variable.
    - The 'openai' and 'pyperclip' Python packages.
    """
    openai.api_key = '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'  # Replace with your actual API key

    messages = [{
        "role": "system",
        "content": "You are a helpful assistant trained in civil engineering. You provide professional, accurate, and practical advice on civil engineering topics."
    }]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        ai_response = response.choices[0].message['content']
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})

        # Copy AI response to clipboard
        pyperclip.copy(ai_response)

if __name__ == "__main__":
    chat()
