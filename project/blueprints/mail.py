import smtplib

from flask import Blueprint, Response, request
import json
import ipdb

from facade.celery_service import send_email_to_mom

mail_endpoints = Blueprint("mail_endpoints", __name__)

@mail_endpoints.route("/send_mail", methods=["POST"])
def send():
    # ipdb.sset_trace()
    data = json.loads(request.data)
    send_email_to_mom.delay(data["origin"], data["destiny"], data["pwd"], data["message"])
    return Response({"message": "Mail sended!!"}, status=200)