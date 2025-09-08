import requests
API_KEY = "23932f6c1f362018392551e35a8bfbd3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter your city: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=ua"
response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("Error")
else:
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    print(f"Weather in the city {city}: {temp}°C, feels like {feels}°C, {description}")