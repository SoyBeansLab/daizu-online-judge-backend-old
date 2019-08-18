from typing import List, Union

import psycopg2

# from domain.User.user import User
from interface.database.sqlhandler import Cursor as AbsCursor
from interface.database.sqlhandler import Result as AbsResult
from interface.database.sqlhandler import SqlHandler as AbsSqlHandler


class Result(AbsResult):
    def __init__(self, rowid: int):
        self.last_insertid = rowid

    def lastrowid(self) -> int:
        return self.last_insertid


class Cursor(AbsCursor):
    def __init__(self, cursor):
        self.cursor = cursor

    def fetch_all(self):
        # def fetch_all(self) -> Union[List[User]]:
        # return self.cursor.fetchall()
        return self.cursor

    def fetch_one(self):
        # def fetch_one(self) -> Union[User]:
        # return self.cursor.fetchone()
        return self.cursor[0]


class SqlHandler(AbsSqlHandler):
    def __init__(self, dbname: str):
        # 環境から取るようにする
        self.host = "database"
        self.dbname = dbname
        self.user = "daizu"
        self.password = "soybeanslab"
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
            )
        except psycopg2.OperationalError as err:
            raise err
        # self.cursor = self.connection.cursor()

    def execute(self, query: str, *args) -> Result:
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            lastrowid = cursor.lastrowid()
        self.connection.commit()
        return lastrowid

    def query(self, query: str, *args) -> Cursor:
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            data = cursor.fetchall()
        return Cursor(data)
