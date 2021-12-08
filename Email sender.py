import smtplib

sender = 'sabretest7@gmail.com' #  will be replaced with my real email address

password = 'Maz1keen!' #  will be replaced with my real password

receivers = ['darren.pratt@sabrerail.com']

message = """From: Sabre Test <sabretest7@gmail.com>
To: Darren Pratt <darren.pratt@sabrerail.com>
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