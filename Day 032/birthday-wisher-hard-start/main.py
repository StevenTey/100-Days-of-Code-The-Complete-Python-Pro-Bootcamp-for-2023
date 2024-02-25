##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

import datetime as dt
import pandas as pd
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
(today_month, today_day) = (dt.datetime.now().month, dt.datetime.now().day)
bd_df = pd.read_csv("birthday-wisher-hard-start/birthdays.csv")
bd_dict = {(row.month, row.day): row for (index, row) in bd_df.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
my_email = "stevenweijun1@gmail.com" 
password = ""

import smtplib
import random

# iterate through each record in bd_dict and check if today matches a birthday in the birthdays.csv
for (month, day) in bd_dict:
    if (today_month, today_day) == (month, day):
        # send the birthday email
        random_letter_int = random.randint(1, 3)
        with open(f"birthday-wisher-hard-start/letter_templates/letter_{random_letter_int}.txt") as letter_file:
            birthday_wish = letter_file.read()
        
        with smtplib.SMTP(host = "smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email, 
                to_addrs= bd_dict[(month, day)]["email"],
                msg = birthday_wish.replace("[NAME]", bd_dict[(month, day)]["name"])
            )


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



