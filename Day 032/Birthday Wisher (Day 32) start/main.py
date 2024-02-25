import smtplib
import datetime as dt
import random

my_email = "stevenweijun1@gmail.com" 
password = 

with open("Birthday Wisher (Day 32) start/quotes.txt") as file:
    quotes = file.readlines()

quote = random.choice(quotes)

if dt.datetime.now().weekday() == 6:
    with smtplib.SMTP(host = "smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email, 
            to_addrs= "steven.tey@klook.com", 
            msg = f"Subject: Quote of the week\n\n{quote}."
        )