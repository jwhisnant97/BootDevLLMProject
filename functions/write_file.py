import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes data passed as argument and writes to file or overwrites existing file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file we are wanting to write to or overwrite.",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="data to write to file passed as string",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):

    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
            pass
        else:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)

        f.close()
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: "{e}"'

