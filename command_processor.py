# command procwssing library

import subprocess
import webbrowser as wb
import os
import pyautogui
from datetime import datetime
import volume_changer
import speaker
import music_list
import music_plyer
import weather_updater

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
# vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
music_path = r"D:\songs\Music(eng)"

profile1 = "Profile 1" # --> gaming
profile2 = "Profile 2" # --> nisargkumar (profectional)
profile3 = "profile 3" # --> college
profile4 = "Default" # --> nisarg

def process_command(command):

    c = command.lower().strip(".").strip().strip(".")

    if "open" in c: # application opening related commands
        if "google" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.google.com"]) # opens google
            # wb.open("https://www.google.com")

        elif "youtube" in c or "you tube" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.youtube.com"]) # opens youtube
            # wb.open("https://www.youtube.com")

        elif "chatgpt" in c or "chat gpt" in c or "charge gpt" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.chatgpt.com"]) # opens chatGPT
            # wb.open("https://www.chatgpt.com")

        elif "linkedin" in c or "linked in" in c or "link in" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.linkedin.com"]) # opens linkedIn

        elif "github" in c or "github" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.github.com"]) # opens GitHub

        else: # unknown command if none of the above are found
            print("unknown command")
            speaker.speak("unknown command")


    elif "search for" in c: # search related commands
        if "on youtube" in c or "on you tube" in c: # search on youtube
            query = c.replace("search for","").replace("on youtube","").strip().replace(" ","+")
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", f"https://www.youtube.com/results?search_query={query}"])
    
        elif "on google" in c: # search on google
            query = c.replace("search for","").replace("on google","").strip().replace(" ","+")
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", f"https://www.google.com/search?q={query}"])
    
    elif "take screenshot" in c or "take screen shot" in c: # takes screenshot
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}.png"
        os.chdir(r"C:\Users\nisar\Pictures\Screenshots")
        screenshot.save(filename) # save screenshot at in screenshot folder in pictures
        speaker.speak("screen shot has been taken")
        print(f"Saved screenshot as {filename}")
    
    elif "volume" in c: # volume related commands
        if "increase" in c: # increases volume
            try:
                l = c.split(" ")
                volume_changer.increase_volume(int(l[3])/100)
                speaker.speak(f"volume increased by {l[3]}")
            except IndexError:
                volume_changer.increase_volume()
                speaker.speak(f"volume increased")

        elif "decrease" in c: # decreases volume
            try:
                l = c.split(" ")
                volume_changer.decrease_volume(int(l[3])/100)
                speaker.speak(f"volume decreased by {l[3]}")
            except IndexError:
                volume_changer.decrease_volume()
                speaker.speak(f"volume decreased")

        elif "unmute" in c: # unmute the volume
            volume_changer.unmute_volume()
            speaker.speak("volume unmuted")

        elif "mute" in c: # mute the volume
            speaker.speak("volume muted")
            volume_changer.mute_volume()

        else: # unknown command if none of the above are found
            print("unknown command")
            speaker.speak("unknown command")
    
    elif "play" in c or "music" in c: # music related commands
        if "play music" in c: # plays music in alphabetical order
            music_plyer.player.play()
        
        elif "play" in c: # plays specific song
            song = c.replace("play ", "")
            music_plyer.player.play_by_name(song)
            # subprocess.Popen([vlc_path, music_path])
            # music_plyer.player.play()
        
        elif "pause" in c: # pauses song
            music_plyer.player.pause()

        elif "resume" in c: # resumes song
            music_plyer.player.resume()

        elif "shuffle" in c or "saffal" in c or "suffolk" in c or "saffron" in c: # turn on-off shuffle mode
            music_plyer.player.shuffle_songs()

        elif "stop" in c: # stops playing music
            music_plyer.player.stop()
            
        else: # unknown command if none of the above are found
            print("unknown command")
            speaker.speak("unknown command")

    
    elif "song" in c:
        if "next" in c: # plays next song
            music_plyer.player.next_song()
        elif "previous" in c: # plays previous song
            music_plyer.player.prev_song()

    elif "weather" in c:
        if "current" in c:
            l1 = c.split(" ")
            city = l1[-1]
            weather_report = weather_updater.get_weather(city)
            speaker.speak(weather_report)

        elif "forecast" in c:
            l1 = c.split(" ")
            city = l1[-1]
            error, weather_report = weather_updater.fetch_forecast(city)
            weather_updater.show_forecast_gui(city,weather_report)

        else:
            print("unknown command")
            speaker.speak("unknown command")


    else: # unknown command if none of the above are found
        print("unknown command")
        speaker.speak("unknown command")
