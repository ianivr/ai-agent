import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        command.extend(args if args else [])

        process_result = subprocess.run(
            command,
            text=True,
            timeout=30,
            cwd=working_dir_abs,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        output_string = ""
        if process_result.returncode != 0:
            output_string += f"Process exited with code {process_result.returncode}\n"
        elif not process_result.stderr and not process_result.stdout:
            output_string += "No output produced\n"
        else:
            if process_result.stdout:
                output_string += "STDOUT: " + process_result.stdout + "\n"
            if process_result.stderr:
                output_string += "STDERR: " + process_result.stderr + "\n"

        return output_string
    except Exception as err:
        return f"Error: executing Python file: {err}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write to, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="List of arguments to pass to the Python file when executing",
            ),
        },
        required=["file_path"],
    ),
)
