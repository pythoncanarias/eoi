# smtpd_senddata.py

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Alex Samarin',
                                    'alejandro.samarin@gmail.com'))
msg['From'] = email.utils.formataddr(('Fake Account',
                                      'fake-account1245@example.com'))
msg['Subject'] = 'Simple test message'

conn = smtplib.SMTP('127.0.0.1', 1025)
# conn.set_debuglevel(True)  # show communication with the server
try:
    conn.sendmail('fake-account1245@example.com',
                    ['alejandro.samarin@gmail.com'],
                    msg.as_string())
finally:
    conn.quit()
