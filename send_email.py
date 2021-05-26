import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

x = smtp_object.ehlo()
print(x)

y = smtp_object.starttls()
print(y)

email = "send_email_id"
password = "sender_email_api_key"

z = smtp_object.login(email, password)
print(z)

from_address = sender_email_id
to_address = reciever_email_id

subject = "Testing Things"
message = "Body of mail"

msg = "Subject: "+subject+'\n'+message
smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()
