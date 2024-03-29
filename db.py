import logging
import threading

from mysql import connector

from settings import (
    mysql_db_name,
    mysql_host,
    mysql_password,
    mysql_pool_name,
    mysql_pool_size,
    mysql_user,
)

logger = logging.getLogger(__name__)




def build_mysql_config():
    return dict(
        pool_name=mysql_pool_name,
        pool_size=mysql_pool_size,
        host=mysql_host,
        user=mysql_user,
        database=mysql_db_name,
        passwd=mysql_password,
        buffered=True
    )


def create_pool():
    return connector.connect(**build_mysql_config())


pool_lock = threading.Lock()
pool = create_pool()


def choose_param(args, kwargs):
    if len(args) > 0:
        return args
    if len(kwargs) > 0:
        return kwargs


def ensure_connection():
    pool_lock.acquire()
    try:
        if not pool.is_connected():
            print("reconnect")
            pool.reconnect()
    except Exception as e:
        logger.error(e)
    finally:
        pool_lock.release()


def execute(args, kwargs, cursor, sql, many=False):
    param = choose_param(args, kwargs)
    if param is None:
        cursor.execute(sql)
    else:
        if many:
            cursor.executemany(sql, param)
        else:
            cursor.execute(sql, param)


def transactional(method):
    def decorator(*args, **kwds):
        ensure_connection()
        try:
            _result = method(*args, **kwds)
            pool.commit()
        except Exception as e:
            pool.rollback()
            raise e
        return _result

    return decorator


def insert(method):

    def decorator(dao, *args, **kwargs):
        ensure_connection()
        cursor = pool.cursor()
        try:
            sql = method(dao, *args, **kwargs)
            execute(args, kwargs, cursor, sql)
            return cursor.lastrowid
        except Exception as e:
            logger.error(e)
        finally:
            cursor.close()
    return decorator


def insert_many(method):

    def decorator(dao, *args):
        ensure_connection()
        cursor = pool.cursor()
        try:
            sql, keys = method(dao, *args)
            params = []
            for param in args[0]:
                params.append(tuple(param[key] for key in keys))
            cursor.executemany(sql, params)
        except Exception as e:
            logger.error(e)
        finally:
            cursor.close()
    return decorator


def query(method):

    def decorator(dao, *args, **kwargs):
        ensure_connection()
        cursor = pool.cursor()
        try:
            sql = method(dao, *args, **kwargs)
            execute(args, kwargs, cursor, sql)
            data = cursor.fetchall()

            return data
        except Exception as e:
            logger.error(e)
        finally:
            cursor.close()
    return decorator


def update(method):

    def decorator(dao, *args, **kwargs):
        ensure_connection()
        cursor = pool.cursor()
        try:
            sql = method(dao, *args, **kwargs)
            execute(args, kwargs, cursor, sql)
            return cursor.rowcount
        except Exception as e:
            logger.error(e)
        finally:
            cursor.close()

    return decorator


def get(method):
    def decorator(dao, *args, **kwargs):
        ensure_connection()
        cursor = pool.cursor()
        try:
            sql = method(dao, *args, **kwargs)
            execute(args, kwargs, cursor, sql)
            return cursor.fetchone()
        except Exception as e:
            logger.error(e)
        finally:
            cursor.close()

    return decorator
