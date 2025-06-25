import subprocess
from os import path

def run_python_file(working_directory, file_path):
    temp_path = path.join(working_directory, file_path)
    cwd_name = path.basename(working_directory)
    abs_directory = path.abspath(temp_path)
    if abs_directory.find(cwd_name) < 0:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not path.exists(abs_directory):
        return f'Error: File "{file_path}" not found.'

    if not abs_directory.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process_cwd = path.abspath(working_directory)

        run_result = subprocess.run(
            ["python3", file_path], 
            input=file_path,
            timeout=30, 
            capture_output=True, 
            cwd=process_cwd,
            text=True
        )

        output = None
        if run_result.stdout is not None:
            output = f"STDOUT: {run_result.stdout}\n"
            output += f"STDERR: {run_result.stderr}\n"
        else:
            output = "No output produced."

        if run_result.returncode != 0:
            output += f"Process exited with code {run_result.returncode}\n"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
