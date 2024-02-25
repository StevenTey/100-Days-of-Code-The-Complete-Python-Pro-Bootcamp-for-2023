import requests
import datetime

MY_LAT = 1.358613
MY_LONG =103.883010

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
time_now = datetime.datetime.now().hour
print(sunrise)
print(time_now)