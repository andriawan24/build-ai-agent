import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    full_path = os.path.join(os.path.abspath(working_directory), file_path)

    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        file_content_string = ""

        with open(full_path, "r") as f:
            file_content_string = f.read()

            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS]
                file_content_string += f"\n\n[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"

        return file_content_string
    except Exception as e:
        return str(e)

    