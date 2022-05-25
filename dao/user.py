import db


class UserDAO:

    @db.insert
    def save(self, **kwargs):
        sql = """INSERT INTO users (name, create_time, modified_time, state)
        VALUES (%(name)s, %(create_time)s, %(modified_time)s, %(state)s)
        """
        return sql

    @db.get
    def find(self, uid: int):
        sql = """SELECT
            id, name, create_time, modified_time, state
            FROM users WHERE id = %s  LIMIT 1"""
        return sql


userDAO = UserDAO()
