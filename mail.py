#!/bin/bash/python3
import smtplib

# Create SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
s.staarttls()

# Suthentication
s.login("sender_email", "sender_pass")

# Message to be sent
message = '''
This mail is to notify the developer that your latest code has been failed, please debug it as soon as possible.
'''

# sendint the mail
s.sendmail("sender_email", "receiver_email", message)

#Terminatiin the session
s.quit()

print("Mail was sent")
