import os
from openai import OpenAI
from dotenv import load_dotenv

import sys

load_dotenv()

api_key = os.getenv("OPEN_AI_SECRET_KEY")
if not api_key:
    raise ValueError("OPEN_AI_SECRET_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

def chat_bot(input_text):
    response = client.responses.create(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        instructions="You are a helpful assistant. Always think step-by-step and answer the user's questions as clearly as possible. Give the answers in a logically and use bullet point or numbered list if possible.",
        input=input_text,
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