import db


class TokenDAO:

    @db.insert
    def save(self, **kwargs):
        sql = """INSERT INTO token
                (token, user_id, create_time, modified_time)
            VALUES
                (%(token)s, %(user_id)s, %(create_time)s, %(modified_time)s)"""
        return sql

    @db.get
    def find(self, token):
        sql = """SELECT
            id, token, user_id, create_time, modified_time, state
            FROM token
            WHERE token = %s LIMIT 1"""
        return sql

    @db.get
    def find_by_user(self, user_id):
        sql = """SELECT
        id, token, user_id, create_time, modified_time, state
        FROM token
        WHERE user_id = %s LIMIT 1"""
        return sql

    @db.update
    def update(self, token, modified_time, token_id):
        sql = "UPDATE token SET token = %s, modified_time = %s WHERE id = %s"
        return sql


tokenDAO = TokenDAO()
