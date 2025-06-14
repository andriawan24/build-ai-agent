import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

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
    is_verbose = any(arg in sys.argv for arg in ["-v", "--verbose"])

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    iters = 0
    while True:
        iters += 1
        if iters > 20:
            print(f"Maximum iterations ({20}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, is_verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

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
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, is_verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if is_verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))

if __name__ == "__main__":
    main()
