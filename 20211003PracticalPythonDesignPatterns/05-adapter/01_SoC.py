import csv

class UserFetcher:
    def __init__(self, src):
        self.src = src

    def fetch_users(self):
        with open(self.src, 'r') as f:
            reader = csv.DictReader(f)
            users = [x for x in reader]
        return users

import smtplib
from email.mime.text import MIMEText

class Mailer:
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipients]

        s = smtplib.SMTP('localhost')
        s.send_message(recipients)
        s.quit()

if __name__ == '__main__':
    u = UserFetcher('users.csv')
    m = Mailer()

    m.send('me@example.com',
            [x['email'] for x in u.fetch_users()],
            'this is your message', 'have a good day'
    )
