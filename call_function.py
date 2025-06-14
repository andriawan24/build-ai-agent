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

    functions = {
        schema_get_file_content.name: get_file_content,
        schema_get_files_info.name: get_files_info,
        schema_write_file.name: write_file,
        schema_run_python_file.name: run_python_file
    }

    function_name = function_call_part.name
    if function_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=functions.name,
                    response={"error": f"Unknown function: {functions.name}"},
                )
            ],
        )
    
    args = dict(function_call_part.args)
    args['working_directory'] = "./calculator"
    result = functions[function_name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )