import types
import logging
import psycopg2
import psycopg2.pool
import psycopg2.extras
from contextlib import contextmanager

from analyzer.utils.config import load_config
from analyzer.utils.argparse import clear_environ

ENV_VAR_PREFIX = 'ANALYZER_'

config = load_config(ENV_VAR_PREFIX)
dbpool = psycopg2.pool.ThreadedConnectionPool(**config)
clear_environ(lambda i: i.startswith(ENV_VAR_PREFIX))

log = logging.getLogger(__name__)

@contextmanager
def pg_cursor() -> None:
    conn = dbpool.getconn()
    log.info('Connected to database')
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        log.info('Rollback cursor')
        raise
    finally:
        log.info('Disconnecting from database')
        dbpool.putconn(conn)
        log.info('Disconnected from database')

def select_query(query: str) -> list:
    with pg_cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return rows

def load_data(query: str, params: tuple) -> None:
    with pg_cursor() as cur:
        cur.execute(query, params)