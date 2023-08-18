# ---------------------------------------------
# making a simple email sender using python
# ---------------------------------------------


# import modules
import getpass
import smtplib
import ssl
from email.message import EmailMessage

# "y.soliman2719@su.edu.eg"

# get the email date from the user
subject = "hello From yossef"
body = "This is a test email form Python! , you can visit or github profile !" 
sender_email = input("Enter a sender email: ")
password = getpass.getpass("Enter a password for sender email: ")
receiver_email = input("Enter a receiver email: ")

# create the message
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# add the body to the message and will show as plain text
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <h4>{body}</h4>
        <p style="padding" 20px 0px;">vist us in github </p>
        <img src='https://user-images.githubusercontent.com/3369400/133268513-5bfe2f93-4402-42c9-a403-81c9e86934b6.jpeg' alt='sticker'>
        <a href='https://github.com/yossefsabry'>github profile</a>    </body>
</html>
"""

# add the html to the message and will show as html 
message.add_alternative(html, subtype="html")


# create a secure SSL context
context = ssl.create_default_context()

# send the email
print("Sending Email!")

# send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    
    # login to the server
    server.login(sender_email, password)
    
    # send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

# print success message
print("Success")

# disconnect from the server
server.quit()
