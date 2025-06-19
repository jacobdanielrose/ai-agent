import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Runs the specified python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the python file to be read is found, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be writen to the specified file path."
            )
        }
    )
)
