import os

from dotenv import load_dotenv
from google import genai
from google.auth import default
from google.genai import types
from google.genai.types import GenerateContentConfig, FunctionDeclaration
from sys import argv

from functions.caller import call_function

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

schema_get_files_info = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description="Gets the content, up to 10000 characters, from the specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to load the contents from. Up to 10,000 characters will be loaded."
            ),
        },
    ),
)

schema_run_python_file = FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run relative to the file from relative to the working directory."
            ),
        },
    )
)

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Write or overwrite file with content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content to."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file."
            )
        },
    )
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

prompt_config = GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

answer = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=prompt_config)
function_call_part = answer.function_calls[0]

# Call the generic function caller dispatch
result = call_function(function_call_part, verbose)
print(f"-> {result.parts[0].function_response.response}")

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")
