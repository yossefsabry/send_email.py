import getpass
import smtplib
import ssl
from email.message import EmailMessage

subject = "hello From yossef"
body = "This is a test email form Python! , you can visit or github profile !" 
sender_email = "y.soliman2719@su.edu.eg"
receiver_email = "y.soliman2719@su.edu.eg"
password = getpass.getpass("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
        <p style="padding" 20px 0px;">vist us in github </p>
        <img src='https://user-images.githubusercontent.com/3369400/133268513-5bfe2f93-4402-42c9-a403-81c9e86934b6.jpeg' alt='sticker'>
        <a href='https://github.com/yossefsabry'>github profile</a>    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")