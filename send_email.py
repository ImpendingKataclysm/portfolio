import smtplib
import ssl

# standard host name
host = "smtp.gmail.com"
# standard port number
port = 465

username = "ktjanzen42@gmail.com"
password = "fotljvyjzqxidzzw"

receiver = "ktjanzen42@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Another test
Hello!
This is a test message
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
