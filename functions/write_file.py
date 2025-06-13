import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(os.path.abspath(working_directory), file_path)

    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(full_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file with the file path provided, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="A file path to the file inside working directory. If not provided just say that we need the valid file to write"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content of a file"
            )
        }
    )
)