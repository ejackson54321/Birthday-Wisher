import pandas as pd
import smtplib
import datetime as dt
import random,os

MY_EMAIL = "ENTER YOUR EMAIL ADDRESS"
PASSWORD = "ENTER YOUR EMAIL PASSWORD"
SENDER = 'ENTER YOUR NAME'

#ADD NEW BIRTHDAY ENTRY
question = input("Do you want to add a birthday? (Y/N): ")
if question.lower() == "y":
    NAME = input("Name: ")
    EMAIL = input("E-Mail: ")
    YEAR = input("Year: ")
    MONTH = input("Month: ")
    DAY = input("Day: ")
    df = pd.DataFrame({'name': [NAME],
       'email': [EMAIL],
       'year': [YEAR],
       'month':[MONTH],
       'day': [DAY]})
    df.to_csv('birthdays.csv', mode='a', index=False, header=False)

#BIRTHDAY TODAY CHECK
now = dt.datetime.now()
month = now.month
today = now.day

data = pd.read_csv("birthdays.csv")
result = data.to_dict()

b_days = {}
for i in range(0, len(result['month'])):
    if result['month'][i] == month and result['day'][i] == today:
        b_days[result['name'][i]] = result['email'][i]

#RANDOM LETTER PICKED FOR EMAIL MESSAGE
if len(b_days) > 0:
    for name, email in b_days.items():
        letter = f"letter_templates/{random.choice(os.listdir('letter_templates'))}"
        with open(letter, "r") as f:
            content = f.readlines()
            content[0] = f'Dear {name},\n'
            content[-1] = f'{SENDER}'

        with open(letter, "w") as f:
            f.writelines(content)

        f = open(letter)
        message = f.read()

#SEND EMAIL
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{message}")





