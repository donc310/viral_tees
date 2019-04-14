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
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
        print('Connected to Gmail account successfully.')

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
        print('- Message has been sent.')

df = pd.read_csv('MMC Brochure.csv', error_bad_lines=False)

for index, row in df.iterrows():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    comp_name = str(row[' Company'])
    print('Email to: ' + comp_name)
    per_name = str(row[' FirstName'])
    print('Email to: ' + per_name)
    rec = str(row[' Email'])
    print('Email to: ' + rec)
    message_body  = 'Hi ' + per_name +',<br><br>We\'re excited to be hosting our Chicago Hotel Investment & Development event on October 10th. In doing some research, I feel that ' + comp_name + ' would be a great fit for one of our panels.<br><br>Are you free anytime this week or next for a call to discuss the opportunity?<br><br>Best, <br><br>Sam Markovich'

    gm = Gmail('sam.markovich@bisnow.com', 'pass', rec)
    gm.send_message('Bisnow Meeting: ' + per_name + ' - Hotel Investment & Development Event', message_body)
    print('-- Message for ' + rec + ' (' + comp_name + ') is completed.')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('*********************************')
print('Finish reading through CSV.')
print('*********************************')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
