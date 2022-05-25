

import logging

from flask import Blueprint
from utils import generate_uuid


user = Blueprint("user", __name__)

logger = logging.getLogger(__name__)


@user.route("/uuid", methods=["GET"])
def uuid():
    return generate_uuid()
