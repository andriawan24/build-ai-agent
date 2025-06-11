import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(os.path.abspath(working_directory), directory)

    if directory.startswith("..") or directory.startswith("/"):
        raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(full_path):
        raise ValueError(f'Error: "{directory}" is not a directory')
    
    dirs = os.listdir(full_path)

    results = []

    for dir in dirs:
        doc_path = os.path.join(full_path, dir)
        is_dir = os.path.isdir(doc_path)
        size = os.path.getsize(doc_path)

        results.append({"name": dir, "file_size": size, "is_dir": is_dir})

    formatted_result = ""

    for i in range(len(results)):
        formatted_result += f"- {results[i]["name"]}: file_size={results[i]["file_size"]} bytes, is_dir={results[i]["is_dir"]}"
        if i != len(results) - 1:
            formatted_result += "\n"

    return formatted_result