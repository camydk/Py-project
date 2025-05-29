#!/usr/bin/env python3

import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Weather in {city}: {response.text}")
        else:
            print("Failed to fetch weather info.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
