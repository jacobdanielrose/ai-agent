import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    content = ""
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
        if len(content) == 10000:
            content += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error opening file: {e}"

    return content
