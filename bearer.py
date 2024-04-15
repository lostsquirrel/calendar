import logging

from flask_httpauth import HTTPTokenAuth

from service import user as userService

auth = HTTPTokenAuth(scheme='Bearer')


@auth.get_user_roles
def get_user_roles(user):
    if user.id == 1:
        return 'admin'
    return 'user'


@auth.verify_token
def verify_token(token):
    _token = userService.getToken(token)
    if _token is not None:
        user = userService.getUser(_token.user_id)
        return user
    logging.error(f'token is invalid {token}')