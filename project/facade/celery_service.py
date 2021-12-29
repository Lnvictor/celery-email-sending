import datetime

from celery import Celery
from celery.schedules import crontab

from .mail_service import send_mail

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def send_email_to_mom(origin, destiny, pwd, message):
    return send_mail(origin, destiny, pwd, message)


def schedule_service(origin, destiny, pwd, message, day, hour, minute):
    time = datetime.datetime.utcnow() + datetime.timedelta(
        days=day, hours=hour, minutes=minute
    )
    send_email_to_mom.apply_async((origin, destiny, pwd, message), eta=time)

    # app.conf.beat_schedule = {
    #     "add_weekly_schedule": {
    #         "task": "celery.service.send_email_to_mom",
    #         "schedule": crontab(day_of_week=day, hour=hour, minute=minute),
    #         "args": (origin, destiny, pwd, message),
    #     }
    # }


app.conf.timezone = "UTC"
