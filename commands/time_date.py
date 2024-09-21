#Get Current time and date

import datetime
import pyttsx3

def tell_time_date():
    engine = pyttsx3.init()

    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %B %d, %Y")

    engine.say(f"The Current time is {current_time}")
    engine.say(f"Today's date is {current_date}")
    engine.runAndWait()

if __name__ == '__main__':
    tell_time_date()