from typing import List

from domain.Contest.usecase.contest_repository import (
    ContestRepository as AbsContestRepository,
)
from domain.Contest.contest import Contest
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ContestRepository(AbsContestRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self) -> List[Contest]:
        rows = self.sqlhandler.query("SELECT * FROM contests").fetch_all()
        return [Contest(*row) for row in rows]

    def find(self, contest_id: str) -> Contest:
        row = self.sqlhandler.query(
            "SELECT * FROM contests WHERE contest_id=%s", (contest_id,)
        ).fetch_one()
        if len(row) == 0:
            return None
        return Contest(*row)
