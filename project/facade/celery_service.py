from datetime import timedelta
from celery import Celery
from celery.schedules import crontab, solar

from .mail_service import send_mail

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_email_to_mom(origin, destiny, pwd, message):
    return send_mail(origin, destiny, pwd, message)

# Testing Scheduling
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'celery.send_email_to_mom',
#         'schedule': timedelta(seconds=5),
#         'args': ()
#     },
# }

app.conf.timezone = 'UTC'