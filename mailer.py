import smtplib
from email.message import EmailMessage

def send_mail(to, subject, body):
    sender = "your_name@gmail.com" # input your email account example: john123@gmail.com
    app_password = " " # Input your google or any mail account password which is 16 digits

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)

send_mail(
    " ", # input the receiver's email address example: jane123@gmail.com
    " ", # input your subject
    """ """ # Compose your message body
)
