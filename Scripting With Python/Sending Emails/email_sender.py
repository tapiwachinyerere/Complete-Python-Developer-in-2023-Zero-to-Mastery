import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tapiwa Chinyerere'
email['to'] = 'leonamagaya@gmail.com'
email['Subject'] = 'Ko wambohwa here?'

email.set_content('Ko ndini ndatumira email ino ngePython zve nhai hama yangu.')

with smtplib.SMTP(
    host='smtp.gmail.com',
    port=587
) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('chinyereretapiwa@gmail.com', 'frcw xooi tjnc zbae')
    smtp.send_message(email)