import smtplib
import pandas as pd


class Gmail(object):
    def __init__(self, email, password, recepient):
        self.email = email
        self.password = password
        self.recepient = recepient
        self.server = 'smtp.gmail.com'
        self.port = 465
        session = smtplib.SMTP_SSL(self.server, self.port)
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.recepient,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.recepient,
            headers + "\r\n\r\n" + body)
