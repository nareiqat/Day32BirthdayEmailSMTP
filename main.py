import smtplib
import datetime as dt
import pandas as pd
import random

GMAIL = "someemail@gmail.com"
PASSWORD = "password"

data = pd.read_csv('birthdays.csv')
today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        x = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(from_addr=GMAIL, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{x}")
