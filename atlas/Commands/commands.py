import os
import subprocess
from pyttsx3 import speak
from atlas.Commands import Folder_commands

APP_PATHS = {
    # Browsers
    "chrome": "chrome",
    "google": "chrome",
    "google chrome": "chrome",
    "browser": "chrome",

    # Terminals
    "cmd": "start cmd",
    "command prompt": "start cmd",
    "terminal": "start cmd",
    "shell": "start cmd",

    # Jupyter Notebook
    "jupyter": "start cmd /k jupyter notebook",
    "jupyter notebook": "start cmd /k jupyter notebook",
    "notebook": "start cmd /k jupyter notebook",

    # VS Code
    "code": "code",
    "visual studio code": "code",
    "vs code": "code",
    "vs": "code",

    # Python
    "python": "start cmd /k python",
    "run python": r"python",
    "python atlas": r"start cmd /k P:\\Anaconda\\envs\\ml_env\\python.exe",

    # Spyder IDE
    "spyder": "spyder",
    "spyder ide": "spyder",

    # RStudio
    "rstudio": "rstudio",
    "r studio": "rstudio",

    # Git Bash
    "git bash": "git-bash",
    "bash": "git-bash",

    # Anaconda Navigator
    "anaconda": "anaconda-navigator",
    "anaconda navigator": "anaconda-navigator",
    "navigator": "anaconda-navigator",

    # Excel
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "ms excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "spreadsheet": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",

    # PowerPoint
    "powerpoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "microsoft powerpoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "slides": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "ppt": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",

    # Word
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "microsoft word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "docs": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",

    # File Explorer
    "explorer": "explorer",
    "file explorer": "explorer",
    "open folder": "explorer",

    # Calculator
    "calculator": "calc",
    "calc": "calc",

    # Notepad
    "notepad": "notepad",
    "notes": "notepad",
}


def open_pc_app(command):
        command = command.lower()

        for app in APP_PATHS:
            if app in command:
                path = APP_PATHS[app]
                try:
                    if "launch" in command:
                        speak(f"Opening: {app}")

                        if path.lower().endswith(".exe") and os.path.isfile(path):
                            subprocess.Popen([path])

                        elif os.path.isdir(path):
                            os.startfile(path)

                        else:
                            os.system(path)
                    return

                except Exception as e:
                    speak(f" Failed to open {app}: {e}")
                    return

        speak("App not recognized in command.")


def get_process_name_from_path(command):
    # if 'close' in command:
    #
    #
    # exit_code = os.system(f'taskkill /f /im "{known_processes[app_key]}"')
    #
    # if exit_code == 0:
    #     speak(f"{app} has been closed.")
    # else:
    #     speak(f"Failed to close {app}. It may not be running.")
    pass