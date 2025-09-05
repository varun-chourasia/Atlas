from tts import speak, wishme, take_command
from atlas.Commands import atlas_playback as playback
from atlas.Commands import Folder_commands, commands

# ---------- Main Entry ----------
if __name__ == "__main__":
    wishme()

    while True:
        print(f"\n[Passive Mode] Waiting for wake word 'jarvis'...")
        wake_command = take_command().lower()

        if wake_command is None:
            print("No valid input. Retrying...")
            continue

        if "nova" in wake_command:
            speak("Yes? What should I do?")
            actual_command = take_command()

            if actual_command is None:
                speak("Sorry, I didn't catch that.")
                continue

            actual_command = actual_command.lower()

            if actual_command.startswith("play "):
                playback.play_song_from_command(actual_command)

            elif actual_command.startswith("open"):
                if "folder" in actual_command:
                    Folder_commands.open_folder(actual_command)

            elif actual_command.startswith("launch"):
                    commands.open_pc_app(actual_command)

            elif actual_command.startswith("close"):
                commands.get_process_name_from_path(actual_command)

            elif "run" in actual_command or "script" in actual_command or actual_command.endswith((".py", ".cpp", ".c")):
                    Folder_commands.open_script_smart(actual_command)


            elif any(exit_cmd in actual_command for exit_cmd in ["exit", "quit", "stop"]):
                speak("Goodbye! Have a great day.")
                break

            else:
                speak("Sorry, I can only play media or open files/folders right now.")

        else:
            print("Wake word not found in command.")
            continue
