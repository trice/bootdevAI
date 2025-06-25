import os
from os import path, listdir

def get_files_info(working_directory, directory=None):
    if directory is not None:
        temp_path = path.join(working_directory, directory)
    else:
        temp_path = working_directory

    cwd_name = path.basename(working_directory)
    abs_directory = path.abspath(temp_path)
    if abs_directory.find(cwd_name) < 0:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    
    
    files = listdir(abs_directory)
    result = ""
    for file in files:
        full_file_name = path.join(abs_directory, file)
        is_dir = path.isdir(full_file_name)
        if not is_dir:
            file_size = path.getsize(full_file_name)
        else:
            file_size = 0
        result += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return result 
