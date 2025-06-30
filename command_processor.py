import subprocess
import webbrowser as wb
import os

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

profile1 = "Profile 1" # --> gaming
profile2 = "Profile 2" # --> nisargkumar (profectional)
profile3 = "profile 3" # --> college
profile4 = "Default" # --> nisarg

def process_command(c):
    if "open google" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.google.com"])
        # wb.open("https://www.google.com")

    elif "open youtube" in c.lower() or "open you tube" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.youtube.com"])
        # wb.open("https://www.youtube.com")

    elif "open chatgpt" in c.lower() or "open chat gpt" in c.lower() or "open charge gpt" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile4}", "https://www.chatgpt.com"])
        # wb.open("https://www.chatgpt.com")

    elif "open linkedin" in c.lower() or "open linked in" in c.lower() or "open link in" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.linkedin.com"])

    elif "open github" in c.lower() or "open github" in c.lower():
        subprocess.Popen([brave_path, f"--profile-directory={profile2}", "https://www.github.com"])

    else:
        print("unknown command")
