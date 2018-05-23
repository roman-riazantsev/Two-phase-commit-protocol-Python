#!/usr/bin/python
import psycopg2
from src.commands import *


def make_payment(conn, table, payment_info):
    try:
        cur = conn.cursor()
        cur.execute(UPDATE[table].format(*payment_info))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))
        sys.exit(1)
    else:
        print('\'{1}\'USD was successfully withdrawn from \'{0}\' account'.format(*payment_info))


def register_book_info(conn, table, info):
    try:
        cur = conn.cursor()
        cur.execute(INSERT_INTO[table].format(*info))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))
    else:
        print('booking_data \'{}\' added to table \'{}\''.format(info, table))

