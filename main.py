import os
import sys
from dotenv import load_dotenv
from google import genai
from sys import argv

if len(argv) < 2:
    print("Error: no prompt provided")
    exit(1)
    
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
answer = client.models.generate_content(model="gemini-2.0-flash-001", contents=f"{argv[1]}")
print(answer.text)
print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")