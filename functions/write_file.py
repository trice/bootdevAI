from os import path

def write_file(working_directory, file_path, content):
    temp_path = path.join(working_directory, file_path)
    cwd_name = path.basename(working_directory)
    abs_directory = path.abspath(temp_path)
    if abs_directory.find(cwd_name) < 0:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(abs_directory, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: "{e}"'
