#!/usr/bin/python3
"""send email from windows"""

import smtplib

SENDER_EMAIL =  'useremail@gmail.com'
SENDER_PASSWORD = 'password'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendemail(SENDER_EMAIL, receiver_email, message)
