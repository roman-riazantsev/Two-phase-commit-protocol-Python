import psycopg2
import sys
import pandas as pd
import pandas.io.sql as psql

from src.settings import DATABASES


def show():
    connection = psycopg2.connect(**DATABASES["db1"])
    # my_table   = pd.read_sql_table('table_name', connection)
    my_table = pd.read_sql('select * from fly_booking', connection)

    print(my_table)

    #
    # try:
    #     cur = connections['flights_db'].cursor()
    #     cur.execute("SELECT * from fly_booking;")
    #     connections['flights_db'].commit()
    #     rows = cur.fetchall()
    #     for row in rows:
    #         print("   ", row)
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print('Error {0}'.format(error))
    #     sys.exit(1)
    #
    # try:
    #     cur = connections['hotels_db'].cursor()
    #     cur.execute("SELECT * from hotel_booking;")
    #     connections['hotels_db'].commit()
    #     rows = cur.fetchall()
    #     for row in rows:
    #         print("   ", row)
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print('Error {0}'.format(error))
    #     sys.exit(1)
    #
    # try:
    #     cur = connections['accounts_db'].cursor()
    #     cur.execute("SELECT * from account;")
    #     connections['accounts_db'].commit()
    #     rows = cur.fetchall()
    #     for row in rows:
    #         print("   ", row)
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print('Error {0}'.format(error))
    #     sys.exit(1)