import smtplib
import decouple


def send_mail(origin, destiny, pwd, message):
    s = smtplib.SMTP(host=decouple.config("MAIL_HOST"), port=decouple.config("MAIL_PORT"))
    s.starttls()
    s.login(origin, pwd)
    return s.sendmail(origin, destiny, message)

