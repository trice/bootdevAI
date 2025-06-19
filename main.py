import os
from pyexpat.errors import messages
from tabnanny import verbose

from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv

if len(argv) < 2:
    print("Error: no prompt provided")
    exit(1)

verbose = False
if len(argv) > 2:
    if argv[2].lower() == "--verbose":
        verbose = True

user_prompt = argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]    
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
answer = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(answer.text)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")