import json
import requests

def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
# URL of the weather API
api_url = 'https://api.example.com/weather'

# Fetch the weather data
weather_data = fetch_weather_data(api_url)

if weather_data:
    # Save the data to a file
    save_json(weather_data, 'weather_data.json')

    # Read the data back into a dictionary
    saved_weather_data = read_json('weather_data.json')

    # Use the data
    print(saved_weather_data)