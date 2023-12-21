import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'ME' 
email['to'] = 'YOU' #insert email adress you are sending to
email['Subject'] = 'Insert Subject'

email.set_content(html.substitute(name = 'Blah'), 'html')

with smtplib.SMTP(
    host='smtp.gmail.com',
    port=587
) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Insert Your Email Address', 'Insert Your Password')
    smtp.send_message(email)
    print('Email Sent!')