from dao.calendar import calendarDAO
from domain.calendar import Calendar


def list(user_id: int):
    rows = calendarDAO.find(user_id)
    if rows is not None:
        return [Calendar(*row) for row in rows]
    return []
