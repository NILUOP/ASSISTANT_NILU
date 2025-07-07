import requests
import api
from plyer import notification
import tkinter as tk
from tkinter import ttk


API_KEY = api.weather_api
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

# this function gives current weather of the given city
# takes city name as input

def get_weather(city):
    # featch data using api
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return f"Error: {data['error']['message']}", None
        
    # take important parts of the feathced data
    location = data['location']['name']
    region = data['location']['region']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_kph = data['current']['wind_kph']
    wind_dir = data['current']['wind_dir']


    message = (
        f"Weather in {location}, {region}:\n"
        f"Temp: {temp_c}°C\n"
        f"Condition: {condition}\n"
        f"Humidity: {humidity}%\n"
        f"Wind: {wind_kph} km/h {wind_dir}"
    )

    # gives notification of the weather
    notification.notify(
        title=f"weather in {location}, {region}",
        message=f"Temp: {temp_c}°C\n"
                f"Condition: {condition}\n"
                f"Humidity: {humidity}%\n"
                f"Wind: {wind_kph} km/h {wind_dir}",
        timeout=10  # seconds
    )

    return message

# this function featch fore cast data for GUI function to show
# takes city name as the input
def fetch_forecast(city):
    params = {
        "key": API_KEY,
        "q": city,
        "days": 3,
        "aqi": "no",
        "alerts": "no"
    }

    try:
        # featch data using api
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return f"Error: {data['error']['message']}", None

        forecast_data = []

        # generates all 3 pages
        for i, day in enumerate(data["forecast"]["forecastday"]):
            date = day["date"]
            lines = [f"\n\nHourly Forecast for {city.title()}, {data["location"]["region"]}, {data["location"]["country"]} on {date}:\n"]
            
            # data which is going to show in each page
            for hour in day["hour"]:
                time = hour["time"].split(" ")[1]
                temp = hour["temp_c"]
                condition = hour["condition"]["text"]
                humidity = hour["humidity"]
                wind = hour["wind_kph"]
                wind_dir = hour["wind_dir"]
                lines.append(f"{time} → {temp}°C, {condition}, Humidity: {humidity}%, Wind: {wind} km/h {wind_dir}")
            forecast_data.append((f"Day {i+1} - {date}", "\n".join(lines)))

        return None, forecast_data

    except Exception as e:
        return f"Exception: {str(e)}", None

# this function generate GUI for the forecast data
def show_forecast_gui(city, forecast_data):

    root = tk.Tk()
    root.lift()               # Bring window to front
    root.focus_force()        # Force focus on the window
    root.after(1000, lambda: root.attributes('-topmost', False))  # Stay on top briefly
    root.attributes('-topmost', True)


    root.title(f"3-Day Forecast for {city.title()}")
    root.geometry("850x620")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    for title, content in forecast_data:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=title)

        text_area = tk.Text(frame, wrap=tk.WORD, font=("Courier", 10))
        text_area.insert(tk.END, content)
        text_area.config(state=tk.DISABLED)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)

    root.mainloop()
