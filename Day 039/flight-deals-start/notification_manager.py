import requests
from twilio.rest import Client

account_sid = "ACdc27a6785b17277a1abf60a3e9fd86b5"
auth_token = "29e2b84bcb66c3933a213f73a1fd8802"
client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body = "This is a test message o0o o0o",
#     from_ = "+13257503261",
#     to = "+6592340324"
# )

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass

    def send_sms(self, message):
        message = client.messages.create(
            body = message,
            from_ = "+13257503261",
            to = "+6592340324"
        )
        print(message.sid)