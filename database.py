import sqlite3


class Database:
    # Opens database connection.
    def __init__(self, name):

        try:
            self.connect = sqlite3.connect(name)
            self.cursor = self.connect.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database.")

    # Inserts user data into database.
    def insert(self, login, email, password):

        self.cursor.execute("INSERT INTO USERS (login, email, password) VALUES (?, ?, ?)", (login, email, password))

    # Creating table in database if not exists.
    def create(self, table_name):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS '{}'"
                            "(ID INTEGER PRIMARY KEY, LOGIN TEXT, EMAIL TEXT, PASSWORD TEXT)".format(table_name))

    # Closes database connection.
    def close(self):

        if self.connect:
            self.connect.commit()
            self.cursor.close()
            self.connect.close()
