# Greet the user 

import pyttsx3 

def greet_user():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say("Hello I am Jarvis, How can i assist you today?")
    engine.runAndWait()

if __name__ == "__main__":
    greet_user()