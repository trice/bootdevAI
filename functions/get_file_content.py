from os import path

def get_file_content(working_directory, file_path):
    temp_path = path.join(working_directory, file_path)
    cwd_name = path.basename(working_directory)
    abs_directory = path.abspath(temp_path)
    if abs_directory.find(cwd_name) < 0:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not path.isfile(abs_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_directory, 'r') as file:
            file_data = file.read(10000)
            if len(file_data) == 10000:
                file_data += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_data
    except Exception as e:
        return f'Error: "{e}"'
