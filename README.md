<!-- # ASSISTANT_NILU

personal voice assistant

more info will be added later :) -->

# 🧠 ASSISTANT_NILU – Personal Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/github/license/NILUOP/ASSISTANT_NILU)

## 🎯 Overview

**ASSISTANT_NILU** is a powerful, Python-based personal voice assistant designed to perform a wide range of tasks using voice commands. From opening apps and browsing websites to giving weather updates and searching the internet, this assistant streamlines your desktop interaction with a simple "Hi Nilu!"

---

## 🚀 Features

- 🎙️ **Voice Command Interface** – Speak naturally to control your system
- 🌐 **Web Search** – Google, YouTube, Wikipedia, and more
- 📅 **Time & Date** – Speak the time and date with ease
- 🧠 **AI Capabilities** – Interact with OpenAI's GPT for smarter responses
- 🗺️ **Weather Forecast** – Get weather updates with city and day inputs
- 🔊 **Text-to-Speech** – Human-like voice output using `pyttsx3`
- 📂 **File & App Launching** – Open any installed apps or files
- 📸 **Camera & Screenshot** – Take photos or screenshots using voice
- 🗃️ **Clipboard Management** – Read copied content aloud
- 🎶 **Play Music** – Open and play media from local storage
- 🧪 **Utilities** – Battery status, system info, and more

---

## 🛠️ Requirements

Ensure you have Python 3.x installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

## Key Libraries:

- speech_recognition

- pyttsx3

- openai

- pyautogui

- requests

- tkinter

- datetime

- bs4

- geopy

- weather-api

And more (see requirements.txt)

🧑‍💻 Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/NILUOP/ASSISTANT_NILU.git
cd ASSISTANT_NILU
Set your OpenAI API key in the appropriate file.

Run the main file:

bash
Copy
Edit
python main.py
Start speaking! Example commands:

“weather forecast of Delhi”

“Open YouTube”

“take a screenshot”

“play song/music”

"increase/decrease volume"
```
📁 Project Structure
bash
Copy
Edit
ASSISTANT_NILU/
├── main.py                 # Entry point for the assistant
├── voice.py                # Voice recognition and TTS
├── gpt_module.py           # OpenAI integration
├── weather_gui.py          # Weather forecast GUI
├── helper_functions.py     # Reusable utility methods
├── requirements.txt
└── README.md
```
## 🧠 AI Capabilities
This assistant integrates with OpenAI GPT to answer general queries. Make sure to provide your API key in the openai section for full functionality.

## 🪄 Customization

### Want to add your own commands or features? Explore and modify:

commands.py: Add new functions and voice triggers

weather_gui.py: Update layout or city options

main.py: Adjust assistant’s workflow or add new features

## 📃 License
This project is licensed under the MIT License – feel free to modify and distribute with credit.

## 🙌 Acknowledgements
Developed by NILUOP with love and Python.

## 🤝 Contributions
Pull requests and suggestions are welcome! Fork the repo, improve it, and create a PR.

## 📬 Contact
For any queries or collaboration opportunities, feel free to open an issue or contact via GitHub.