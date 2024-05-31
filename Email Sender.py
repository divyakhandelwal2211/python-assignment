import smtplib
try:
    server = smtplib.SMTP(host = 'SMTP.gmail.com', port = 587)
    server.starttls()                                 #start server
    recever_email = input('enter the email')          
    sender_email = 'itsdivya2211@gmail.com'
    password = 'hppf ydlt arxp jgsc'
    server.login(sender_email, password =password)
    subject = input('enter the message')
    body = input('enter the msg')
    message = f"subject: {subject}\n\n{body}"
    server.sendmail(sender_email,recever_email,message)
    print('email sent')
    server.quit()

except Exception as e:
    print('email not sent')