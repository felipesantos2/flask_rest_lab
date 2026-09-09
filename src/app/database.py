"""
Python and SQlite docs:
        https://docs.python.org/3/library/sqlite3.html
"""

# import sqlite3

# con = sqlite3.connect("banco.sqlite3")
# cur = con.cursor()
#
# import mysql.connector

# cnx = mysql.connector.connect(
#     user="scott", password="password", host="127.0.0.1", database="employees"
# )
# cnx.close()


class MySQL:
    def connect(self):
        pass


class SQLite:
    def connect(self):
        pass

class DatabaseFactory:
    def __init__(self, driver="sqlite") -> None:
        self.driver = driver

    def connection(self):
        if self.driver == "sqlite":
            return SQLite().connect()

        return MySQL().connect()
