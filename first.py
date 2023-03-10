import requests
import json
city = input("Enter a city name: ")
api_key = "74561596cc1565dbcf4e258dafc2746d"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    temperature = data['main']['temp']-273
    print(temperature)
    pressure = data['main']['pressure']
    print(pressure)
    humidity = data['main']['humidity']
    print(humidity)
    wind_speed = data['wind']['speed']
    print(wind_speed)
    weather_description = data["weather"][0]["description"]
    print(weather_description)
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.reason}")
