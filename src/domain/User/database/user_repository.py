from typing import List

from domain.User.usecase.user_repository import (
    UserRepository as AbsUserRepository,
)
from domain.User.user import User
from infrastructure.database.postgres.sqlhandler import SqlHandler


class UserRepository(AbsUserRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def store(self, user: User) -> int:
        if len(self.find(user)):
            return False

        self.sqlhandler.execute(
            "INSERT INTO users (username) VALUES (%s)", (user.username,)
        )
        # error
        return True

    def find_all(self) -> List[User]:
        rows = self.sqlhandler.query("SELECT username FROM users").fetch_all()
        # error
        return [User(row[0]) for row in rows]

    def find(self, user: User) -> List[User]:
        rows = self.sqlhandler.query(
            "SELECT username FROM users WHERE username=%s", (user.username,)
        ).fetch_all()
        return [User(row[0]) for row in rows]
