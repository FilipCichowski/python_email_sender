# -*- coding: utf-8 -*-
import smtplib, ssl, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

def readContent(path):
  with open(path, encoding='utf8') as f:
    f.readline() # ommit first line in file
    temp = ''.join(line.rstrip() for line in f)
    return temp

def readSubject(path):
   with open(path, encoding='utf8') as f:
    firstLine = f.readline()
    subject = firstLine.replace("Subject: ", "")
    return subject

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "highflyersemailsender@gmail.com" # change to desired sender's mail

message = MIMEMultipart("alternative")
message["Subject"] = readSubject("./content.txt")
message["From"] = sender_email

text = readContent('./content.txt')
html = readContent('./content_html.txt')

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

try:
    password = getpass()
    with open('./receivers.json') as file:
        receivers = json.load(file)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            for receiver in receivers:
                message["Bcc"] = receiver['mail']
                server.send_message(message, sender_email, receiver['mail'])
                print("Sent e-mail to ", receiver['mail'])
except Exception:
    print('Wrong password')
