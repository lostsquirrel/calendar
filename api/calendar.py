import logging

from bearer import auth
from flask import Blueprint, request
from service import calendar as calendarService
from utils import render_json
calendar = Blueprint("calendar", __name__)

logger = logging.getLogger(__name__)


@calendar.route("/list", methods=["GET"])
@auth.login_required
def list():
    user = auth.current_user()
    calendars = calendarService.list(user.id)
    return render_json(calendars)
