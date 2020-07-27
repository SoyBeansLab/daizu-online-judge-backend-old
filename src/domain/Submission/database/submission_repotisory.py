from typing import List

from domain.Submission.usecase.submission_repository import (
    SubmissionRepository as AbsSubmissionRepository,
)
from domain.Submission.submission import Submission
from infrastructure.database.postgres.sqlhandler import SqlHandler


class SubmissionRepository(AbsSubmissionRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def store(self, submission: Submission) -> int:
        return self.sqlhandler.execute(
            """
            INSERT INTO submissions (
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
            submission.submit_id,
            submission.submit_date,
            submission.username,
            submission.problem_id,
            submission.language,
            submission.test_case,
            submission.source_code,
        )

    def find_all(self, problem_id: str) -> List[Submission]:
        rows = self.sqlhandler.query(
            "SELECT * FROM submissions WHERE problem_id=%s", (problem_id,)
        ).fetch_all()
        return [Submission(*row) for row in rows]

    def find(self, submit_id: str) -> Submission:
        row = self.sqlhandler.query(
            "SELECT * FROM submissions WHERE submit_id=%s", (submit_id,)
        ).fetch_one()
        if len(row) == 0:
            return None
        return Submission(*row)
