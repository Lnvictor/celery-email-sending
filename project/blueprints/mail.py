import json

from flask import Blueprint, request

from facade.celery_service import schedule_service, send_email_to_mom

mail_endpoints = Blueprint("mail_endpoints", __name__)


@mail_endpoints.route("/send_mail", methods=["POST"])
def send():
    data = json.loads(request.data)
    send_email_to_mom.delay(
        data["origin"], data["destiny"], data["pwd"], data["message"]
    )
    return {"message": "Mail sended!!"}


@mail_endpoints.route("/schedule_mail", methods=["POST"])
def schedule():
    data = json.loads(request.data)
    schedule_service(
        data["origin"],
        data["destiny"],
        data["pwd"],
        data["message"],
        data["day"],
        data["hour"],
        data["minute"],
    )

    return {"message": "Mail Scheduled"}
