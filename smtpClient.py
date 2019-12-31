import smtplib, ssl
#python -m smtpd -c DebuggingServer -n localhost:1025

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Type your mail adress and press enter: ")

password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

receiver_email = "batumailservice@gmail.com"
message = """\
Subject: Batu test

hocam valla yaptim"""


# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()