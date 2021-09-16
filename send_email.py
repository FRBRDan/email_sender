import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path
import sys

addressee_email = sys.argv[1]
addressee_name = sys.argv[2]

# Setting up basic parameters
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dan Farber'
email['to'] = addressee_email
email['subject'] = 'Testing of email through Python.'

# Substituting the $name with the actual name
email.set_content(html.substitute(name = addressee_name), 'html')

# Basic SMTP use
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('frbrdan@gmail.com', 'MyPassword')
    smtp.send_message(email)
    print('Email sent!')