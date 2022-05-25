
from flask import Flask

from api.calendar import calendar
from api.user import user
from api.event import event
from utils import LogicException, ValidationError, render_error

app = Flask(__name__)

app.register_blueprint(calendar, url_prefix='/calendar')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(event, url_prefix='/event')
app.register_error_handler(
    ValidationError, lambda e: render_error(str(e), 400))
app.register_error_handler(
    LogicException, lambda e: render_error(e.value, e.code))
