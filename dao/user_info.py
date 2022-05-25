import db


class UserInfoDAO:

    @db.insert
    def save(self, **kwargs):
        sql = """INSERT INTO user_info
        (user_id, pregnancy, menstruation_period, full_period,
        firstweekday,
            create_time, modified_time, state)
        VALUES
        (%(user_id)s, %(pregnancy)s, %(menstruation_period)s, %(full_period)s,
        %(firstweekday)s,
            %(create_time)s, %(modified_time)s, %(state)s)
        """
        return sql

    @db.get
    def find_by_user(self, uid: int):
        sql = """SELECT
            id, user_id, pregnancy, menstruation_period, full_period,
            firstweekday,
            create_time, modified_time, state
            FROM user_info WHERE user_id = %s  LIMIT 1"""
        return sql


userInfoDAO = UserInfoDAO()
