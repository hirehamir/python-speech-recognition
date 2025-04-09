import pyperclip  # type: ignore
import speech_recognition as sr  # type: ignore
from utils.print_with_time import print_with_time

recognizer = sr.Recognizer()
try:
    while True:
        with sr.Microphone() as source:
            print()
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print_with_time("Recording until you stop talking...")
            recorded_audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(recorded_audio, language="en-US")
            print_with_time(f'I heard, "{text}".')
            pyperclip.copy(text)
            print_with_time(f'"{text}" copied to clipboard\n')
        except sr.UnknownValueError:
            print_with_time("Speech Recognition could not understand audio.\n")
        except sr.RequestError as ex:
            print(f"Could not request results; {ex}")
except OSError as ex:
    print_with_time(f"Operating System Error: {ex}")
