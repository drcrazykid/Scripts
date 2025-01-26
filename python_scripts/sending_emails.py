#!/usr/bin/python3

# How to Send Email from Python
# You will need your own smtp server to actually send

import smtplib
from email import message

from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


from_addr = inputFromAddr
to_addr = inputToAddr
subject = 'I just sent this email from Python!'
content = 'How neat is that!'

def send_regMsg():

    msg = message.Message()

    msg.add_header('from',from_addr)
    msg.add_header('to',to_addr)
    msg.add_header('subject', subject)
    body = content
    msg.set_payload(body)

    server = smtplib.SMTP(inputServer, serverPort)
    server.login(from_addr, addrPassword)

    server.send_message(msg, from_addr=from_addr,to_addrs=[to_addr])



# EXTRA: Send email using an attachment
def send_msgAttachment():
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    filename = 'test.txt'
    with open(filename, 'r') as f:
        attachment = MIMEApplication(f.read(), Name=basename(filename))
        attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

    msg.attach(attachment)

    server = smtplib.SMTP(inputServer, serverPort)
    server.login(from_addr, addrPassword)

    server.send_message(msg, from_addr=from_addr,to_addrs=[to_addr])