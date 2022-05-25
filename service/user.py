
from dao.token import tokenDAO
from dao.user import userDAO
from dao.user_info import userInfoDAO
from domain.token import Token
from domain.user import User
from domain.user_info import UserInfo


def getToken(token: str) -> Token:
    _t = tokenDAO.find(token)
    if _t is not None:
        return Token(*_t)


def getUser(user_id: int) -> User:
    row = userDAO.find(user_id)
    if row is not None:
        return User(*row)


def getUserInfo(user_id: int) -> UserInfo:
    row = userInfoDAO.find_by_user(user_id)
    if row is not None:
        return UserInfo(*row)
