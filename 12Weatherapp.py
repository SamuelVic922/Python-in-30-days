# We are building a Weather App today (19/08/2025) using OpenWeatherMap API

import requests

print("Welcome to the Weather App")
print("Bringing you the most accurate Weather Reports , no matter your region")
print("________________________________________________________")
print("\n")


def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            "Error fetching data:, {response.status_code}- {response.json().get('message', 'Unknown error')}")
        return None


global_countries = ["Nigeria", "United States", "Canada",
                    "India", "Japan", "South Africa"]


print("What will you like to do today")
print("1. See major countries Weather")
print("2. Check your Country's Weather")

api_key = "9834b339c0051810be54788b4648c077"
global_countries = ["Nigeria", "United States", "Canada",
                    "India", "Japan", "Australia"]

try:
    user_input = int(input("What is your Choice: "))
except ValueError:
    print("Invalid input , please choose a valid number")


if user_input == 1:
    for country in global_countries:
        weather_data = get_weather_data(country, api_key)
        if weather_data:
            print(f"\n Weather in {weather_data['name']}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(
                f"Condition: {weather_data['weather'][0]['description']}")
        else:
            print(f"⚠️ Skipping {country} due to error.")
elif user_input == 2:
    weather = input(
        "Which Country's Weather do you want to check today: ")
    weather_data = get_weather_data(weather, api_key)
    if weather_data:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print("Error , choice not recognized")
    exit()
