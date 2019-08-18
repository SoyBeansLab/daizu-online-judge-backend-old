from typing import List

from domain.Problem.usecase.problem_repository import (
    ProblemRepository as AbsProblemRepository,
)
from domain.Problem.problem import Problem
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ProblemRepository(AbsProblemRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self, contest_id: str) -> List[Problem]:
        rows = self.sqlhandler.query(
            "SELECT * FROM problems WHERE contest_id=%s", (contest_id,)
        ).fetch_all()
        return [Problem(*row) for row in rows]

    def find(self, problem_id: str) -> Problem:
        row = self.sqlhandler.query(
            "SELECT * FROM problems WHERE problem_id=%s", (problem_id,)
        ).fetch_one()
        return Problem(*row)
