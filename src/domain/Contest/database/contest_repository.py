from typing import List

from domain.Contest.usecase.contest_repository import (
    ContestRepository as AbsContestRepository
)
from domain.Contest.contest import Contest
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ContestRepository(AbsContestRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self) -> List[Contest]:
        rows = self.sqlhandler.query(
            "SELECT * FROM contest"
        ).fetch_all()
        return [Contest(*row) for row in rows]

    def find(self, contest_id: str) -> Contest:
        rows = self.sqlhandler.query(
            "SELECT * FROM contest WHERE contest_id=%s", (contest_id,)
        ).fetch_all()
        return [Contest(*row) for row in rows]
