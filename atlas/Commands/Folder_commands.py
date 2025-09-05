import os
import subprocess
from atlas.Software.tts import *
import tempfile
import sys

def open_folder(command):
    command = command.lower()
    target = command.replace("open", "").replace("folder", "").strip()

    drives = [r"D:\\", r"E:\\"]

    for drive in drives:
        print(f"Searching in {drive}...")
        for root, dirs, _ in os.walk(drive):
            for dir_name in dirs:
                if target in dir_name.lower():
                    full_path = os.path.join(root, dir_name)
                    speak(f"Folder Found at path {full_path}. Now I'm opening the folder: ")
                    os.startfile(full_path)
                    return

    speak("Folder not found on D or E drive.")

def normalize_spoken_extensions(command: str) -> str:
    """
    Converts spoken file type references to actual extensions.
    Example: "list python" → "list.py"
    """
    replacements = {
        " dot p y": ".py",
        " dot c p p": ".cpp",
        " dot cpp": ".cpp",
        " dot c": ".c",
        " dot python": ".py",
        " python": ".py",
        " c plus plus": ".cpp",
        " c file": ".c",
        " cpp": ".cpp",
        " c": ".c"
    }

    for phrase, ext in replacements.items():
        if phrase in command:
            command = command.replace(phrase, "").strip() + ext
            break

    return command


def open_script_smart(command):
    # Step 1: Preprocess command
    command = command.lower().replace("run", "").replace("script", "").strip()
    command = normalize_spoken_extensions(command)

    # Step 2: Prepare search targets
    known_extensions = [".py", ".cpp", ".c", ".html", ".js", ".css", ".java", ".ipynb", ".txt"]
    words = command.split()

    if len(words) == 1 and any(words[0].endswith(ext) for ext in known_extensions):
        target_name, target_ext = os.path.splitext(words[0])
        search_names = [(target_name, target_ext)]
    else:
        base = "_".join(words)
        search_names = [(base, ext) for ext in known_extensions]

    # Step 3: Search for file in drives
    drives = [r"D:\\", r"E:\\"]

    for drive in drives:
        print(f"Searching in {drive}...")
        for root, _, files in os.walk(drive):
            for file in files:
                name, ext = os.path.splitext(file)
                for target, expected_ext in search_names:
                    if name.lower() == target.lower() and ext.lower() == expected_ext:
                        full_path = os.path.join(root, file)
                        speak(f"Opening {file} in Visual Studio Code...")
                        subprocess.Popen(f'code "{full_path}"', shell=True)

                        # Then also run it
                        if ext == ".py":
                            subprocess.run([sys.executable, full_path])
                        elif ext in [".c", ".cpp"]:
                            compile_and_run_c_cpp(full_path, ext)
                        return

    speak("Script not found on D or E drive.")


def compile_and_run_c_cpp(file_path, ext):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_exe = os.path.join(tempfile.gettempdir(), base_name + ".exe")
    compiler = "g++" if ext == ".cpp" else "gcc"
    compile_cmd = [compiler, file_path, "-o", output_exe]

    speak("Compiling...")
    result = subprocess.run(compile_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        speak("Compilation failed:")
        speak(result.stderr)
        return

    speak("Running executable...")
    subprocess.run([output_exe])
