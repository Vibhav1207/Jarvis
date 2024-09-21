import speedtest
import pyttsx3

def check_network():
    engine = pyttsx3.init()

    # Initialize the speed test
    st = speedtest.Speedtest()
    
    engine.say("Checking network speed, please wait.")
    engine.runAndWait()
    
    
    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000  

    
    engine.say(f"Download speed is {download_speed:.2f} megabits per second")
    engine.say(f"Upload speed is {upload_speed:.2f} megabits per second")
    engine.runAndWait()

    return download_speed, upload_speed

if __name__ == "__main__":
    check_network()
