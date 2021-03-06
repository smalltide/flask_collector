from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "smalltides@gmail.com"
    from_password = ""
    to_email = email

    subject = "Height data"
    message = f"""Hey there, your height is <strong>{height}</strong>
        Average height of all {count} users is {average_height}"""

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
