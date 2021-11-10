# -*- coding: utf-8 -*-
import smtplib, ssl, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = 'Jolene12345!'  # IMPORTANT: delete it later!

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "highflyersemailsender@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Very important test"
message["From"] = sender_email


# text = """\
# Cześć,

# Polecam "Przesłanie Pana Cogito" Herberta.

# Idź dokąd poszli tamci do ciemnego kresu
# po złote runo nicości twoją ostatnią nagrodę

# idź wyprostowany wśród tych co na kolanach
# wśród odwróconych plecami i obalonych w proch

# ocalałeś nie po to aby żyć
# masz mało czasu trzeba dać świadectwo

# bądź odważny gdy rozum zawodzi bądź odważny
# w ostatecznym rachunku jedynie to się liczy

# """
# html = """\
# <html>
#   <body>
#     <h1>Cześć, <br></h1>
#     <p>
#        Polecam "Przesłanie Pana Cogito" Herberta. <br>
#        <br>
#        Idź dokąd poszli tamci do ciemnego kresu <br>
#         po złote runo nicości twoją ostatnią nagrodę <br>
#         <br>
#         idź wyprostowany wśród tych co na kolanach <br>
#         wśród odwróconych plecami i obalonych w proch <br>
#         <br>
#         ocalałeś nie po to aby żyć <br>
#         masz mało czasu trzeba dać świadectwo <br>
#         <br>
#         bądź odważny gdy rozum zawodzi bądź odważny <br>
#         w ostatecznym rachunku jedynie to się liczy <br>
#     </p>
#   </body>
# </html>
# """

# with open('./content.txt', encoding='utf8') as f:
#     subject=f.readline()       # strip title line
#     text=''.join(line.rstrip() for line in f)

# with open('./content_html.txt', encoding='utf8') as f:
#     subject=f.readline()       # strip title line
#     html=''.join(line.rstrip() for line in f)

def readContent(path):
  with open(path, encoding='utf8') as f:
    subjec = f.readline()
    temp = ''.join(line.rstrip() for line in f)
    return temp

text = readContent('./content.txt')
html = readContent('./content_html.txt')

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with open('./receivers.json') as file:
    receivers = json.load(file)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        for receiver in receivers:
            message["To"] = receiver['mail']
            server.sendmail(sender_email, receiver['mail'], message.as_string())
            print("Sent e-mail to ", receiver['mail'])
