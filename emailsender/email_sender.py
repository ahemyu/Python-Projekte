import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


#oioxwtlwlyalciig

html = Template(Path('index.html').read_text())

email = EmailMessage()  # email objekt anlegen
email['from'] = 'Hideaki Miyazaki'
email['to'] = 'emovic@hotmail.de'
email['subject'] = "You have biggest dicku"

email.set_content(html.substitute({'name': 'Schwanz'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  #
    smtp.ehlo()  # Hello at beginning
    smtp.starttls()   # TlsVerschlüsselung
    smtp.login('lobilski3838@gmail.com', 'oioxwtlwlyalciig')  # in m1 acc einloggen
    smtp.send_message(email) # email senden



