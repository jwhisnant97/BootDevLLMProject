import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
            pass
        else:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(*args)
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)

        cp_str = ""

        if completed_process.returncode != 0:
            cp_str += f"Process exited with code {completed_process.returncode}\n"
        if not completed_process.stdout or completed_process.stderr:
            cp_str += "No output produced\n"
        cp_str += f"STDOUT: {completed_process.stdout}"
        cp_str += f"STDERR: {completed_process.stderr}"

        return cp_str

    except Exception as e:
        return f"Error: executing Python file: {e}"