from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python import run_python_file
from functions.get_file_content import get_file_content

from google.genai import types


def call_function(function_call_part, verbose=False):
   if verbose:
      print(f"Calling function: {function_call_part.name}({function_call_part.args})")
   else:
      print(f" - Calling function {function_call_part.name}")

   function_name = function_call_part.name

   function_result = None

   match function_call_part.name:
      case "get_file_content":
         function_result =  get_file_content("./calculator", **function_call_part.args) 
      case "get_files_info":
         function_result =  get_files_info("./calculator", **function_call_part.args) 
      case "write_file":
         function_result =  write_file("./calculator", **function_call_part.args) 
      case "run_python_file":
         function_result =  run_python_file("./calculator", **function_call_part.args)

   if function_result is None:
      function_result = types.Content(
         role="tool",
         parts=[
            types.Part.from_function_response(
               name=function_name,
               response={"error": f"Unknown function: {function_name}"},
            )
         ],
      )
   else:
      function_result = types.Content(
         role="tool",
         parts=[
            types.Part.from_function_response(
               name=function_name,
               response={"result": function_result},
            )
         ],
      )

   return function_result
