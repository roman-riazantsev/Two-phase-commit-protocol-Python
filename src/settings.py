DATABASES = {
    'default': {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'roman',
        'password': '0000'
    },
    'db1': {
        'host': 'localhost',
        'database': 'db1',
        'user': 'roman',
        'password': '0000'
    },
    'db2': {
        'host': 'localhost',
        'database': 'db2',
        'user': 'roman',
        'password': '0000'
    },
    'db3': {
        'host': 'localhost',
        'database': 'db3',
        'user': 'roman',
        'password': '0000'
    }
}

CREATE_TABLES_COMMANDS = {
    'db1': (
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
    ), 'db2': (
        """
        CREATE TABLE Hotel_Booking (
            Booking_ID serial PRIMARY KEY,
            Client_Name character varying,
            Hotel_Name character varying,
            Arrival date,
            Departure date
        )
        """
    ), 'db3': (
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

DEFAULT_DATA_INSERT_COMMANDS = {
    'db1': (
        """INSERT INTO Fly_Booking(Client_Name, Fly_Number, \"From\", \"To\", Date)
            VALUES( \'Nik\',\'KLM 1382\',\'KBP\',\'AMS\',\'01/05/2015\')"""
    ), 'db2': (
        """INSERT INTO Hotel_Booking(Client_Name, Hotel_Name, Arrival, Departure)
            VALUES( \'Nik\',\'Hilton\',\'01/05/2015\',\'07/05/2015\')"""
    ), 'db3': (
        """INSERT INTO Account(Client_Name, Amount)
            VALUES(\'Nik\',200)"""
    )
}

INSERT_DATA_COMMANDS = {
    'db1': (
        """INSERT INTO Fly_Booking(Client_Name, Fly_Number, \"From\", \"To\", Date)
            VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\')"""
    ), 'db2': (
        """INSERT INTO Hotel_Booking(Client_Name, Hotel_Name, Arrival, Departure)
            VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\')"""
    ), 'db3': (
        """INSERT INTO Account(Client_Name, Amount)
            VALUES(\'{0}\',{1})"""
    )
}


