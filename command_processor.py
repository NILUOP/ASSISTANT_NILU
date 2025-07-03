import subprocess
import webbrowser as wb
import os
import pyautogui
from datetime import datetime
import volume_changer
import speaker
import music_list
import music_plyer

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
music_path = r"D:\songs\Music(eng)"

profile1 = "Profile 1" # --> gaming
profile2 = "Profile 2" # --> nisargkumar (profectional)
profile3 = "profile 3" # --> college
profile4 = "Default" # --> nisarg

def process_command(command):

    c = command.lower().strip(".").strip().strip(".")

    if "open" in c:
        if "google" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.google.com"])
            # wb.open("https://www.google.com")

        elif "youtube" in c or "you tube" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.youtube.com"])
            # wb.open("https://www.youtube.com")

        elif "chatgpt" in c or "chat gpt" in c or "charge gpt" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.chatgpt.com"])
            # wb.open("https://www.chatgpt.com")

        elif "linkedin" in c or "linked in" in c or "link in" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.linkedin.com"])

        elif "github" in c or "github" in c:
            subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.github.com"])

        else:
            print("unknown command")
            speaker.speak("unknown command")


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
    
    elif "play" in c or "music" in c:
        if "play music" in c:
            music_plyer.player.play()
        
        elif "play" in c:
            song = c.replace("play ", "")
            music_plyer.player.play_by_name(song)
            # subprocess.Popen([vlc_path, music_path])
            # music_plyer.player.play()
        
        elif "pause" in c:
            music_plyer.player.pause()

        elif "resume" in c:
            music_plyer.player.resume()

        elif "shuffle" in c or "saffal" in c or "suffolk" in c or "saffron" in c:
            music_plyer.player.shuffle_songs()

        elif "stop" in c:
            music_plyer.player.stop()
            
        # else:
        #     song = c.replace("play", "")
        #     subprocess.Popen([vlc_path, music_list.eng_music[song]])

    
    elif "song" in c:
        if "next" in c:
            music_plyer.player.next_song()
        elif "previous" in c:
            music_plyer.player.prev_song()


    else:
        print("unknown command")
        speaker.speak("unknown command")
