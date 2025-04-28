import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import tools
import json

load_dotenv(override = True,)

api_key = os.getenv("OPEN_AI_SECRET_KEY")
# print(f"API Key: {api_key}")
if not api_key:
    raise ValueError("OPEN_AI_SECRET_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

def parse_llm_response(response):
    # Check if the response contains a function call
    if response.output and response.output[0].type == "function_call":
        function_name = response.output[0].name
        arguments = json.loads(response.output[0].arguments)
        expression = arguments.get("expression", None)
        # print(f"Function Name: {function_name}")
        # print(f"Arguments: {arguments}, {type(arguments)}")
        # print(f"Expression: {expression}")
        
        # Call the appropriate function based on the function name
        if function_name == "calculator_tool":
            from calculator_tool import calculator_tool
            result = calculator_tool(expression)
            return result

    # If the response is a text message, return the text content
    elif response.output and response.output[0].type == "message":
        message = response.output[0].content[0].text
        return message
    
def chat_bot(input_text):
    response = client.responses.create(
        model='gpt-3.5-turbo',
        temperature=0, 
        max_output_tokens=150,
        tools=tools,
        tool_choice="auto",
        input=input_text,
    )

    message = parse_llm_response(response)    
    return message


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