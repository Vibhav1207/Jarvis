import os
import sys
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from commands.greet_user import greet_user
from commands.time_date import tell_time_date
from commands.network_check import check_network

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Sorry, I didn't catch that. Please repeat...")
        return "None"

    return query.lower()

def display_network_speed(download_speed, upload_speed):
    
    root = tk.Tk()
    root.geometry("300x100+1000+0")  
    root.title("Network Speed")

    label = tk.Label(root, text=f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps", font=("Arial", 14))
    label.pack()

    root.after(5000, root.destroy) 
    root.mainloop()

def startup_sequence():
    engine = pyttsx3.init()
    
    engine.say("Initializing all systems.")
    engine.say("Checking network connection.")
    engine.runAndWait()

  
    download_speed, upload_speed = check_network()
    display_network_speed(download_speed, upload_speed)

   
    engine.say("Good morning. I am Jarvis, at your service.")
    engine.runAndWait()

def run_jarvis():
    startup_sequence()  

    while True:
        command = take_command()

        if "greet" in command:
            greet_user()

        elif "time" in command or "date" in command:
            tell_time_date()

        elif "exit" in command or "quit" in command:
            print("Goodbye!")
            sys.exit()

        else:
            print("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    run_jarvis()
