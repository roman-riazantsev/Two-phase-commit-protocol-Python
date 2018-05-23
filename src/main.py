#!/usr/bin/python
import psycopg2
import sys

from src.settings import DATABASES
from src.booking import make_payment, register_book_info
from src.initializer import initialize
from src.showData import show


def tpc(connections, booking_info):
    for db in connections:
        connections[db].tpc_begin(connections[db].xid(1, 'Global transaction ID', 'connection to {0}_db'.format(db)))

    try:
        make_payment(connections['accounts_db'], 'account', booking_info['payment'])
        connections['accounts_db'].tpc_prepare()

        register_book_info(connections['flights_db'], 'fly_booking', booking_info['flight'])
        connections['flights_db'].tpc_prepare()

        register_book_info(connections['hotels_db'], 'hotel_booking', booking_info['hotel'])
        connections['hotels_db'].tpc_prepare()

        for db in connections:
            connections[db].tpc_commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Error {0}'.format(error))

        for db in connections:
            connections[db].tpc_rollback()

        sys.exit(1)
    else:
        print("flight & hotel was successfully booked")


def main():
    initialize()
    connections = {'flights_db': psycopg2.connect(**DATABASES["db1"]),
                   'hotels_db': psycopg2.connect(**DATABASES["db2"]),
                   'accounts_db': psycopg2.connect(**DATABASES["db3"])}

    booking_info = {
        'flight': ['Nik', 'KLM 1382', 'KBP', 'AMS', '01/05/2015'],
        'hotel': ['Nik', 'Hilton', '01/05/2015', '07/05/2015'],
        'payment': ['Nik', 100]
    }

    tpc(connections, booking_info)
    print()

    show()

if __name__ == '__main__':
    main()
