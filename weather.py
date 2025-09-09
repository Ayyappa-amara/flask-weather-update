from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="vizianagaram"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&units=metric&q={city}'
    # return request_url
    wheather_data = requests.get(request_url).json()
    return wheather_data

if __name__ == "__mine__":
    print("\n Get Current Wheather Data \n")
    city = input("\n Please Enter City Name \n")
    # check for empty strings and string with empty spaces
    if not bool(city.strip()):
        city = "vizianagaram"
    weather = get_current_weather(city)
    print("\n")
    pprint(weather)