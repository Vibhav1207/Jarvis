import speech_recognition as sr 
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.CYAN + "I am Listning...", end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)

def Trans_hindi_to_english(txt):
    english_txt = translate(txt,to_language="en-in")
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold= 0.4
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.CYAN + "I am Listning...", end="",flush=True)
            try:
                 audio = recognizer.listen(source, timeout=None)
                 print("\r"+Fore.LIGHTYELLOW_EX + "Got it , Recognizing..", end="",flush=True)
                 recognize_txt = recognizer.recognize_google(audio).lower()
                 if recognize_txt:
                    trannslated_txt = Trans_hindi_to_english(recognize_txt)
                    print("\r"+Fore.BLUE + "Mr Vibhav : " + trannslated_txt)
                    return trannslated_txt
                 else :
                     return ""
            except sr.UnknownValueError:
                recognize_txt = ""
            finally:
                print("\r",end="",flush=True)

            os.system("cls" if os.name == "nt" else "clear")
            #treading part
            listen_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=listen)
            listen_thread.start()
            print_thread.start()
            listen_thread.join()
            print_thread.join()


while True:
    listen()