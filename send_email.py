import smtplib
import ssl
import streamlit as st


def send_email(message):
    # standard host name
    host = "smtp.gmail.com"
    # standard port number
    port = 465

    username = st.secrets["username"]
    password = st.secrets["password"]

    receiver = st.secrets["receiver"]
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

