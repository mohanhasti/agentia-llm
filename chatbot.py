import os
from openai import OpenAI
from dotenv import load_dotenv

import sys

load_dotenv(override = True,)

api_key = os.getenv("OPEN_AI_SECRET_KEY")
print(f"API Key: {api_key}")
if not api_key:
    raise ValueError("OPEN_AI_SECRET_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)


def generate_prompt(user_input):
    operations = ["+", "-", "*", "/", "Add", "plus", "minus", "Subtract", "Multiply", "Divide", "Square", "Square Root"]
    
    if any( op in user_input for op in operations):
        return ( "You are a helpful assistant. If the user asks for a math operation or calulation like 15+23, politely refuse to do the math and say suggest to use a calculator tool instead.\n\n"
                f"User: {user_input}\nAssistant"
        )
    else:
        return ( "You are a helpful assistant. Always think step-by-step and answer the user's questions as clearly as possible."
                " Give the answers in a logically and use bullet point or numbered list if possible.\n\n"
                f"User: {user_input}\nAssistant"
        )
        
def chat_bot(input_text):
    response = client.responses.create(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        max_output_tokens=150,
        input=generate_prompt(input_text),
    )

    return response.output_text


def main():
    print("Welcome to the Agentia-LLM Chatbot!")
    print("Type your question or type 'exit' to quit the chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_bot(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()