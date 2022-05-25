import db


class CalendarDAO:

    @db.insert
    def save(self, **kwargs):
        sql = """
        INSERT INTO `calendar`
            (`name`, `user_id`, `create_time`, `modified_time`, `state`)
        VALUES
            (%(name)s`, %(user_id)s`, %(create_time)s`, %(modified_time)s`,
            %(state)s`);
        """
        return sql

    @db.query
    def find(self, uid: int):
        sql = """
        SELECT id, name, user_id, create_time, modified_time, state
        FROM calendar
        WHERE user_id = %s
        """
        return sql


calendarDAO = CalendarDAO()
