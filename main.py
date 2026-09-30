import os

import requests

import time

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API = os.getenv("WEATHER_API")

city = "Ufa"


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"
while True:
    try:
        response = requests.get(url)
        temperature = response.json()["main"]["temp"]
        wind = response.json()["wind"]["speed"]
        message = f"Температура: {temperature}°C \nВетер: {wind} m/s"
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
              json={"chat_id": CHAT_ID, "text": message})
    except Exception as e:
        print( f"Ошибка выполнения: {e}")
    time.sleep(100)

