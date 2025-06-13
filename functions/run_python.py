import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    full_path = os.path.join(os.path.abspath(working_directory), file_path)

    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    result = subprocess.run(
        ["python3", full_path],
        timeout=30,
        capture_output=True,
        text=True,
        check=True
    )

    result_text = ""

    try:
        if result.stdout == "":
            result_text += "STDOUT: No output produced."
        else:
            result_text += f"STDOUT: {result.stdout}"
        
        if result.stderr != "":
            result_text += f"\nSTDERR: {result.stderr}"
    except subprocess.CalledProcessError as e:
        result_text += f"Process exited with code {e.returncode}"
        result_text += f"Error: executing Python file: {e}"

    return result_text

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute provided python file from the path, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="A file path to the python inside working directory. If not provided just say that we need the valid file to run"
            )
        }
    )
)