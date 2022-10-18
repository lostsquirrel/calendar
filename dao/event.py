from datetime import date
import db


class EventDAO:

    @db.insert
    def save(self, **kwargs):
        sql = """
        INSERT INTO events
            (`title`, `description`, `calendar_id`,
            `create_time`, `modified_time`, `state`,
            `start_date`, `end_date`, `start_time`, `end_time`,
            `recurrence`)
        VALUES (
            %(title)s, %(description)s, %(calendar_id)s,
            %(create_time)s, %(modified_time)s, %(state)s,
            %(start_date)s, %(end_date)s, %(start_time)s, %(end_time)s,
            %(recurrence)s);
        """
        return sql

    @db.insert_many
    def batch_save(self, dataset):
        sql = """
        INSERT INTO events
            (`title`, `description`, `calendar_id`,
            `create_time`, `modified_time`, `state`,
            `start_date`, `end_date`, `start_time`, `end_time`,
            `recurrence`)
        VALUES (
            %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s, %s,
            %s);
        """
        keys = (
            "title", "description", "calendar_id",
            "create_time", "modified_time", "state",
            "start_date", "end_date", "start_time", "end_time",
            "recurrence"
        )
        return sql, keys

    @db.query
    def find_by_time_range(self, calendar_id: int, start: date, end: date):
        sql = """SELECT
            id, title, description, calendar_id,
            create_time, modified_time,
            start_date, end_date, start_time, end_time,
            recurrence,
            state
            FROM events
            WHERE calendar_id = %s
            AND (end_date >= %s
                OR start_date <= %s)
        """
        return sql


eventDAO = EventDAO()
