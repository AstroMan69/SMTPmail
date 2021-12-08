import smtplib

sender = 'your email' #  will be replaced with my real email address

password = 'your password' #  will be replaced with my real password

receivers = ['sender']

message = """From: Your name <your email>
To: receivers name <receivers email>
MIME-Version: 1.0
Content-Type: text/html
Subject: Test E-Mail

Test
<a href="http://www.google.com">http://www.google.com</a>
"""

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(sender, password) #  Exception here
try:
    server.sendmail(sender, receivers, message)
    print("Message sent successfully")
except:
    print("Failed to send message")
server.quit()
