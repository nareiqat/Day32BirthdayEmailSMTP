import smtplib
import datetime as dt
import random

gmail = "somemeail@gmail.com"
password = "apassword"
now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

# print(data)

if day_of_week == 3:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        random_quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=password)
        connection.sendmail(from_addr=gmail, to_addrs="dododod@yahoo.com", msg=f"Subject:Thursday Motivation \n\n"
                                                                                f"{random_quote}")
