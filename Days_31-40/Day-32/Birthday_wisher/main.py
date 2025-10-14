

import smtplib
from email.mime.text import MIMEText
import sys
def send_email(letter_):
    msg = MIMEText(letter_)
    msg["Subject"] = "Hello from smtplib"
    msg["From"] = "you@example.com"
    msg["To"] = "someone@example.com"

    with smtplib.SMTP("localhost", 8025) as server:
        server.send_message(msg)

    print(f"SUCCESS :Email sent \n {letter_}!")


from datetime import datetime
today=(datetime.now().day,datetime.now().month)
# or now=datetime.now()
# today=(now.day,now.month)

import pandas
birthday=pandas.read_csv("birthdays.csv")
birthday_dict={(data_row.day,data_row.month):data_row for (index,data_row) in birthday.iterrows()}

if today in birthday_dict:
    birthday_person=birthday_dict[today]
    from random import choice
    file_path=f"letter_templates/letter_{choice(range(1,4))}.txt"
    with open(file_path) as file:
        letter=file.read()
        letter=letter.replace("[NAME]",birthday_person["name"])
    with open("output/ready_to_send.txt","w") as file:
        file.write(letter)
    send_email(letter)






