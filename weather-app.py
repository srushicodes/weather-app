import requests

API_KEY = "520fe521c0ad6e6e690dc8ff340a6ffe"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()

    print("\nWeather Information")
    print("--------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])

else:
    print("Could not find the city.")
    print("Please check the city name.")