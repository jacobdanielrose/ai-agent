import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file to be read is found, relative to the working directory."
            )
        }
    )
)
