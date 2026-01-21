import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import sys


def create_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")
    return genai.Client(api_key=api_key)


def parse_args():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def agent_step(client, messages, verbose=False):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata found in the response.")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return response.text, True

    function_results = []
    for func_call in response.function_calls:
        result = call_function(func_call, verbose=verbose)
        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {func_call.name}")
        function_results.append(result.parts[0])
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
    messages.append(types.Content(role="user", parts=function_results))

    return None, False


def main():
    client = create_client()
    args = parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(20):
        final_text, done = agent_step(client, messages, verbose=args.verbose)
        if done:
            print("Response:", final_text)
            return

    print("Exceeded maximum number of iterations.")
    sys.exit(1)


if __name__ == "__main__":
    main()
