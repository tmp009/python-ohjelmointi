import requests

API_URL = "https://api.chucknorris.io"

joke = None
try:
    joke = requests.get(f"{API_URL}/jokes/random")
except Exception as e:
    print("Error occurred while fetching joke:", e)

if joke.status_code == 200:
  joke_data = joke.json()

  print(joke_data["value"])
