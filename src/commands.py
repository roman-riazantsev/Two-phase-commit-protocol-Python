CREATE_TABLES = {
    'fly_booking': (
        """
        CREATE TABLE Fly_Booking (
            Booking_ID serial PRIMARY KEY,
            Client_Name character varying,
            Fly_Number character varying,
            \"From\" character varying,
            \"To\" character varying,
            Date date
        )
        """
    ), 'hotel_booking': (
        """
        CREATE TABLE Hotel_Booking (
            Booking_ID serial PRIMARY KEY,
            Client_Name character varying,
            Hotel_Name character varying,
            Arrival date,
            Departure date
        )
        """
    ), 'account': (
        """
        CREATE TABLE Account (
            Account_ID serial PRIMARY KEY,
            Client_Name character varying,
            Amount INT,
            CONSTRAINT amount_constraint CHECK (amount >= 0)
        )
        """
    )
}

INSERT_INTO = {
    'fly_booking': (
        """INSERT INTO Fly_Booking(Client_Name, Fly_Number, \"From\", \"To\", Date)
            VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\')"""
    ), 'hotel_booking': (
        """INSERT INTO Hotel_Booking(Client_Name, Hotel_Name, Arrival, Departure)
            VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')"""
    ), 'account': (
        """INSERT INTO Account(Client_Name, Amount)
            VALUES(\'{0}\',{1})"""
    )
}

DROP_DB = {
    'REVOKE': "REVOKE CONNECT ON DATABASE \"{0}\" FROM public;",
    'SELECT': "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = \'{0}\';",
    'DROP': "DROP DATABASE \"{0}\""
}

CREATE_DB = "CREATE DATABASE {0}"

UPDATE = {
    'account': (
        """ UPDATE Account SET Amount = Amount - {1} WHERE Client_Name = \'{0}\';"""
    )
}
