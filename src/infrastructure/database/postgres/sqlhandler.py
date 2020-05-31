import os
from typing import List, Union

import psycopg2

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
        return self.cursor

    def fetch_one(self):
        if len(self.cursor) == 0:
            return []
        return self.cursor[0]


class SqlHandler(AbsSqlHandler):
    def __init__(self):
        # 環境から取るようにする
        self.host = os.getenv("DAIZU_DATABASE_HOST", "")
        self.dbname = os.getenv("DAIZU_DATABASE_NAME", "doj")
        self.user = os.getenv("DAIZU_DATABASE_USERNAME", "daizu")
        self.password = os.getenv("DAIZU_DATABASE_PASSWORD", "soybeanslab")
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
            cursor.execute(query, *args)
            data = cursor.fetchall()
        return Cursor(data)
