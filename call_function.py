from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python import schema_run_python_file, run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, 
        schema_get_file_content, 
        schema_write_file, 
        schema_run_python_file
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    working_directory = "./calculator"

    functions = {
        schema_get_file_content.name: get_file_content,
        schema_get_files_info.name: get_files_info,
        schema_write_file.name: write_file,
        schema_run_python_file.name: run_python_file
    }

    if function_call_part.name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=functions.name,
                    response={"error": f"Unknown function: {functions.name}"},
                )
            ],
        )
    
    result = functions[function_call_part.name](working_directory=working_directory, **function_call_part.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )