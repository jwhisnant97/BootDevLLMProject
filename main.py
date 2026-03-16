import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions



def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        client = genai.Client(api_key=api_key)
        resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],system_instruction=system_prompt),
        )
    if resp.usage_metadata is None:
        raise RuntimeError("No usage metadata. Likely failed API request")
    elif args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")
    print(resp.text)
    if resp.function_calls:
        for function_call in resp.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    
if __name__ == "__main__":
    main()
