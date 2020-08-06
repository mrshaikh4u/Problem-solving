import os.path
import getpass
import mimetypes
from email.message import EmailMessage
import smtplib
file_path = "ProfilePhoto.jpg"
file_name = os.path.basename(file_path)
type , _ = mimetypes.guess_type(file_path)
type , sub_type = type.split('/')
sender = "mohamedrshaikh@gmail.com"
recipient = "aafrahsmulla@gmail.com"
message = EmailMessage()
message["From"] = sender
message["To"] = recipient
message["subject"] ="Mail from python program"
message.set_content("hello this is my first message body")
with open(file_path,'rb') as ap:
    message.add_attachment(ap.read(),maintype = type,subtype=sub_type,filename=os.path.basename(file_name))
print(message)
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
sender = "mohamedrshaikh"
print(mail_server.login(sender,""))
print(mail_server.send_message(message))
mail_server.quit()
