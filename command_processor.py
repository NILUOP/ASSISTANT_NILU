import subprocess
import webbrowser as wb
import os
import pyautogui
from datetime import datetime
import volume_changer
import speaker

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

profile1 = "Profile 1" # --> gaming
profile2 = "Profile 2" # --> nisargkumar (profectional)
profile3 = "profile 3" # --> college
profile4 = "Default" # --> nisarg

def process_command(command):

    c = command.lower().strip(".").strip().strip(".")

    if "open google" in c:
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.google.com"])
        # wb.open("https://www.google.com")

    elif "open youtube" in c or "open you tube" in c:
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.youtube.com"])
        # wb.open("https://www.youtube.com")

    elif "open chatgpt" in c or "open chat gpt" in c or "open charge gpt" in c:
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.chatgpt.com"])
        # wb.open("https://www.chatgpt.com")

    elif "open linkedin" in c or "open linked in" in c or "open link in" in c:
        subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.linkedin.com"])

    elif "open github" in c or "open github" in c:
        subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.github.com"])

    elif "search for" in c:
        if "on youtube" in c or "on you tube" in c:
            query = c.replace("search for","").replace("on youtube","").strip().replace(" ","+")
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", f"https://www.youtube.com/results?search_query={query}"])
    
        elif "on google" in c:
            query = c.replace("search for","").replace("on google","").strip().replace(" ","+")
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", f"https://www.google.com/search?q={query}"])
    
    elif "take screenshot" in c or "take screen shot" in c:
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}.png"
        os.chdir(r"C:\Users\nisar\Pictures\Screenshots")
        screenshot.save(filename)
        speaker.speak("screen shot has been taken")
        print(f"Saved screenshot as {filename}")
    
    elif "volume" in c:
        if "increase" in c:
            try:
                l = c.split(" ")
                volume_changer.increase_volume(int(l[3])/100)
                speaker.speak(f"volume increased by {l[3]}")
            except IndexError:
                volume_changer.increase_volume()
                speaker.speak(f"volume increased")

        elif "decrease" in c:
            try:
                l = c.split(" ")
                volume_changer.decrease_volume(int(l[3])/100)
                speaker.speak(f"volume decreased by {l[3]}")
            except IndexError:
                volume_changer.decrease_volume()
                speaker.speak(f"volume decreased")

        elif "unmute" in c:
            volume_changer.unmute_volume()
            speaker.speak("volume unmuted")

        elif "mute" in c:
            speaker.speak("volume muted")
            volume_changer.mute_volume()

        else:
            print("unknown command")
            speaker.speak("unknown command")

    else:
        print("unknown command")
        speaker.speak("unknown command")
