import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

from src.settings import *
from src.commands import *


def execute_command(db_name, command):
    conn = None
    try:
        conn = psycopg2.connect(**DATABASES[db_name])
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))
        sys.exit(1)
    finally:
        if conn is not None:
            conn.close()


def drop_db(db_name):
    conn = None
    try:
        conn = psycopg2.connect(**DATABASES['default'])
        conn.set_isolation_level(0)
        cur = conn.cursor()

        cur.execute(DROP_DB['REVOKE'].format(db_name))
        cur.execute(DROP_DB['SELECT'].format(db_name))
        cur.execute(DROP_DB['DROP'].format(db_name))

        cur.close()
        print('database \'{0}\' was successfully dropped down'.format(db_name))
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))
        sys.exit(1)
    finally:
        if conn is not None:
            conn.close()


def create_db(db_name):
    conn = None
    try:
        conn = psycopg2.connect(**DATABASES['default'])
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(CREATE_DB.format(db_name))
        conn.commit()
        print('database \'{0}\' successfully created'.format(db_name))
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))
        if conn:
            conn.rollback()
        sys.exit(1)
    finally:
        if conn:
            conn.close()


def initialize():
    for db in ["db1", "db2", "db3"]:
        drop_db(db)
        create_db(db)
        execute_command(db, CREATE_TABLES_COMMANDS[db])
        print()

    execute_command("db3", INSERT_INTO['account'].format('Nik', 500))
