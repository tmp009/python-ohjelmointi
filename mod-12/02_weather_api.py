import requests

API_KEY=""

def get_weather(municipality) -> dict:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&units=metric&appid={API_KEY}")
    if response.status_code == 200:
        return response.json()
    return {}



municipality = input("Enter municipality name: ")
weather = get_weather(municipality)

print(f"Weather: {weather['weather'][0]['description']}")
print(f"Temperature: {weather['main']['temp']} Celsius")
