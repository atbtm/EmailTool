import smtplib
from email.mime.text import MIMEText as text
from emailList import email_list
from time import sleep

file=open("message.txt", "r")
message_body = file.read()

email = input("Your email: ")
password = input("You password: ")
user_name = input("What is your name(first_name + last_name): ")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
print(smtpserver.login(email, password))

#for last_name, email in email_list:
for last_name, email in email_list.items():
    msg = text(message_body.format(last_name, user_name))
    msg['Subject'] = "IN DIRE OF YOUR HELP REGARDING HR1044"
    msg['From'] = email
    msg['To'] = email
    res = smtpserver.sendmail(email, email,msg.as_string())
    print("email for {} has been sent - {}".format(last_name, email))
    sleep(3)

# Remember to disable after running the script
print("Finish! Make sure go to https://myaccount.google.com/u/1/lesssecureapps to disable less secure!")
