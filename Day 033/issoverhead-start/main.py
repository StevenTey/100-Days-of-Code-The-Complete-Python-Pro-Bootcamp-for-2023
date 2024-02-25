import requests
from datetime import datetime

MY_LAT = 1.358613
MY_LONG = 103.883010

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(f"iss_latitude: {iss_latitude}, iss_longitude: {iss_longitude}")
#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# print(f"sunrise: {sunrise}, sunset: {sunset}, time_now: {time_now.hour}")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


my_email = "" 
password = 

import smtplib
import time

is_night = time_now.now().hour > sunset or time_now.hour < sunrise
is_close = abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5

while True:
    time.sleep(60)
    if is_night and is_close:
        with smtplib.SMTP(host = "smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs= "",
                msg = "Subject: Look Up\n\nThe ISS is above you in the sky."
            )
