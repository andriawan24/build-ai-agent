import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from prompts import system_prompt
from call_function import available_functions

model_name = "gemini-2.0-flash-001"

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        print("Please provide an API key")
        exit(1)

    if len(sys.argv) < 2:
        print("Enter a message")
        exit(1)

    user_prompt = sys.argv[1]
    is_verbose = "-v" in sys.argv or "--verbose" in sys.argv

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client=client, messages=messages, is_verbose=is_verbose)

def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions]
        )
    )

    if is_verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    function_call_parts = response.function_calls
    if function_call_parts:
        for function in function_call_parts:
            print(f"Calling function: {function.name}({function.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
