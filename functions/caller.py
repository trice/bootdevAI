from run_python import run_python_file
from get_file_content import get_file_content
from get_files_info import get_files_info
from write_file import write_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function {function_call_part.name}")

    match function_call_part.name:
        case "get_file_content":
           get_file_content("./calculator", **function_call_part.args) 
        case "get_files_info":
           get_files_info("./calculator", **function_call_part.args) 
        case "write_file":
           write_file("./calculator", **function_call_part.args) 
        case "run_python_file":
           run_python_file("./calculator", **function_call_part.args) 
