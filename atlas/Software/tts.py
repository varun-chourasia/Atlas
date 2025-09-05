import speech_recognition as sr
import pyttsx3
import datetime
# ---------- Text-to-Speech (TTS) ----------
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    print(f"ATLAS: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    greeting = "Good morning sir!" if hour < 12 else "Good afternoon sir!" if hour < 18 else "Good evening sir!"
    speak(greeting)
    speak("Please tell me how may I help you?")

def take_command(max_attempts=2, wake_word=None):
    recognizer = sr.Recognizer()

    for attempt in range(max_attempts):
        with sr.Microphone() as source:
            print("🎙️ Listening... (attempt {})".format(attempt + 1))
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = recognizer.listen(source,timeout=3, phrase_time_limit=5)
                print("🧠 Recognizing...")
                command = recognizer.recognize_google(audio, language="en-in")
                print(f"🗣️ Command: {command}")

                command = command.lower()

                if wake_word and wake_word.lower() not in command:
                    print("Wake word not detected.")
                    return None

                return command

            except sr.WaitTimeoutError:
                print("⌛ Timeout: No speech detected.")
                speak("No input detected. Please try again.")
            except sr.UnknownValueError:
                print("❓ Could not understand.")
                speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                print("🚫 Could not request results from Google.")
                speak("Speech recognition service is unavailable.")
                break

    speak("Let's try again later.")
    return None

