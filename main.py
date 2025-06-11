import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Prompt is empty")
        sys.exit(1)

    path = sys.argv[1]

    try:
        print(get_files_info("calculator", path))
    except Exception as e:
        print(e)

    # load_dotenv()

    # prompt = sys.argv[1]
    # is_verbose = "-v" in sys.argv or "--verbose" in sys.argv
    # api_key = os.environ.get("GEMINI_API_KEY")
    # client = genai.Client(api_key=api_key)

    # messages = [
    #     types.Content(role="user", parts=[types.Part(text=prompt)])
    # ]

    # response = client.models.generate_content(
    #     model="gemini-2.0-flash-001",
    #     contents=messages
    # )

    # if is_verbose:
    #     print(f"User prompt: {prompt}")
    #     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # print(response.text)

