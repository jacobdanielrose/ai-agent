import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        output = []
        object = subprocess.run(['python3', abs_file_path], timeout=30, capture_output=True, cwd=abs_working_dir)
        output.append(f'STDOUT: {object.stdout.decode('utf-8')}')
        output.append(f'STDERR: {object.stderr.decode('utf-8')}')
        if object.returncode != 0:
            output.append(f"Process exited with code {object.returncode}")
        result = "\n".join(output)

        if not object.stdout and not object.stderr:
            return 'No output produced'

    except Exception as e:
        return f"Error: executing Python file: {e}"

    return result
