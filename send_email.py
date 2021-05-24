from email.message import Message
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_func(body):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "your@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = 'password@123'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    body = MIMEText(body)
    message.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:

        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
