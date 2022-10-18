

import logging
from datetime import datetime, timedelta

from bearer import auth
from domain.event import Event
from flask import Blueprint, request
from service import event as eventService
from service import user as userService
from utils import Validator, generate_uuid, render_json

event = Blueprint("event", __name__)

logger = logging.getLogger(__name__)


@event.route("/calendar/<calendar_id>", methods=["GET"])
@auth.login_required
def events(calendar_id):
    d = datetime.now()
    user = auth.current_user()
    form = request.args
    year, month = Validator().rule("year", d.year).rule(
        "month", d.month).validate_form(form)
    user_info = userService.getUserInfo(user.id)
    data = eventService.list_range(user_info.firstweekday,
                                   int(calendar_id), int(year), int(month))
    return render_json(data)


@event.route("/calendar/<calendar_id>/menstruation", methods=["POST"])
@auth.login_required
def menstruation(calendar_id):
    user = auth.current_user()
    form = request.get_json()
    d = datetime.now()
    year, month, day = Validator().rule("year", d.year).rule(
        "month", d.month).rule("day", d.date).validate_form(form)
    # menstruation_period =
    start = datetime(year=int(year), month=int(month), day=int(day))
    user_info = userService.getUserInfo(user.id)
    eventService.menstruation_start(calendar_id, start,
                                    user_info.menstruation_period,
                                    user_info.full_period)
    return render_json(None)


@event.route("/calendar/<calendar_id>/pregnancy", methods=["POST"])
@auth.login_required
def pregnancy(calendar_id):
    user = auth.current_user()
    form = request.get_json()
    d = datetime.now()
    year, month, day = Validator().rule("year", d.year).rule(
        "month", d.month).rule("day", d.date).validate_form(form)
    # menstruation_period =
    start = datetime(year=int(year), month=int(month), day=int(day))
    user_info = userService.getUserInfo(user.id)
    eventService.pregnancy_start(calendar_id, start)
    return render_json(None)


@event.route("/calendar/<calendar_id>", methods=["POST"])
@auth.login_required
def normal(calendar_id):
    user = auth.current_user()
    form = request.get_json()
    title, desc, date = Validator().rule("title").rule(
        "description", "").rule("start_date").validate_form(form)
    event_id = eventService.normal(calendar_id,
                                   title, desc,
                                   date, date, None, None)
    return render_json(None)
