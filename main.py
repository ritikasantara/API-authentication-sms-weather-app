import requests

MY_LAT = 23.365971
MY_LNG = 85.341011

api_key = "390fb2acf5fa1df9122eda6850dd2d89"

parameters = {

    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
# print(data["hourly"][0]["weather"][0]["id"])
print(data["hourly"][0]["weather"])
print(data["hourly"][:12])

for value in range(0, len(data["hourly"][:12])):
    if data["hourly"][value]["weather"][0]["id"] < 700:
        print(data["hourly"][value]["weather"][0]["id"])
        print("It's about to rain in your city.\nBring your umbrella.")


# https://api.openweathermap.org/data/2.5/onecall?lat=23.366&lng=85.341&appid=390fb2acf5fa1df9122eda6850dd2d89
# https://api.openweathermap.org/data/2.5/onecall?lat=23.365971&lon=85.341011&appid=390fb2acf5fa1df9122eda6850dd2d89
# https://api.openweathermap.org/data/2.5/onecall?lat=23.365971&lng=85.341011&appid=390fb2acf5fa1df9122eda6850dd2d89






