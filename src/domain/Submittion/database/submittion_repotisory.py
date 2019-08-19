from typing import List

from domain.Submittion.usecase.submittion_repository import (
    SubmittionRepository as AbsSubmittionRepository,
)
from domain.Submittion.submittion import Submittion
from infrastructure.database.postgres.sqlhandler import SqlHandler


class SubmittionRepository(AbsSubmittionRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def store(self, submittion: Submittion) -> int:
        return self.sqlhandler.execute(
            """
            INSERT INTO submittions (
                submit_id,
                submit_date,
                username,
                problem_id,
                language,
                test_case,
                source_code
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            submittion.submit_id,
            submittion.submit_date,
            submittion.username,
            submittion.problem_id,
            submittion.language,
            submittion.test_case,
            submittion.source_code,
        )

    def find_all(self, problem_id: str) -> List[Submittion]:
        rows = self.sqlhandler.query(
            "SELECT * FROM submittions WHERE problem_id=%s", (problem_id,)
        ).fetch_all()
        return [Submittion(*row) for row in rows]

    def find(self, submit_id: str) -> Submittion:
        row = self.sqlhandler.query(
            "SELECT * FROM submittions WHERE submit_id=%s", (submit_id,)
        ).fetch_one()
        if len(row) == 0:
            return None
        return Submittion(*row)
