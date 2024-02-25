import requests
from twilio.rest import Client

LON = 103.82
LAT = 1.35
APIKEY = "c94ef1dd284d8c57b8cfdc67b7c33c91"

account_sid = "ACdc27a6785b17277a1abf60a3e9fd86b5"
auth_token = "29e2b84bcb66c3933a213f73a1fd8802"
client = Client(account_sid, auth_token)

parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": APIKEY,
}

# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# data = request.json()
# print(response.status_code)

# message = client.messages.create(
#     body = "This is a test message o0o o0o",
#     from_ = "+13257503261",
#     to = "+6592340324"
# )

# print(message.sid)