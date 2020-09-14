from typing import List
from datetime import datetime

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

    def find_upcoming(self) -> List[Contest]:
        """ 予定されたContestを取得する """
        rows = self.sqlhandler.query(
            "SELECT * FROM contests WHERE contest_start_date > %s",
            (datetime.now(),),
        ).fetch_all()
        return [Contest(*row) for row in rows]

    def find_current(self) -> List[Contest]:
        """ 開催中のContestを取得する """
        now_date = datetime.now()
        rows = self.sqlhandler.query(
            "SELECT * FROM contests WHERE contest_start_date < %s AND contest_finish_date > %s",
            (now_date, now_date,),
        ).fetch_all()
        return [Contest(*row) for row in rows]

    def find_recent(self) -> List[Contest]:
        """ 終了したContestを取得する """
        rows = self.sqlhandler.query(
            "SELECT * FROM contests WHERE contest_finish_date < %s",
            (datetime.now(),),
        ).fetch_all()
        return [Contest(*row) for row in rows]

    def find(self, contest_id: str) -> Contest:
        row = self.sqlhandler.query(
            "SELECT * FROM contests WHERE contest_id=%s", (contest_id,)
        ).fetch_one()
        if len(row) == 0:
            return None
        return Contest(*row)

    def store(self, contest: Contest) -> None:
        return self.sqlhandler.execute(
            """
                INSERT INTO contests (
                    contest_id,
                    contest_name,
                    contest_start_date,
                    contest_finish_date,
                    contest_time,
                    writer,
                    description,
                    top_content,
                    problem_number
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            contest.contest_id,
            contest.contest_name,
            contest.contest_start_date,
            contest.contest_finish_date,
            contest.contest_time,
            contest.writer,
            contest.description,
            contest.top_content,
            contest.problem_number,
        )

    def update(self, contest_id: str, contest: Contest) -> None:
        return self.sqlhandler.execute(
            """
                UPDATE contests SET
                    contest_id = %s,
                    contest_name = %s,
                    contest_start_date = %s,
                    contest_finish_date = %s,
                    contest_time = %s,
                    writer = %s,
                    description = %s,
                    top_content = %s,
                    problem_number = %s
                WHERE contest_id = %s
            """,
            contest_id,
            contest.contest_name,
            contest.contest_start_date,
            contest.contest_finish_date,
            contest.contest_time,
            contest.writer,
            contest.description,
            contest.top_content,
            contest.problem_number,
            contest_id,
        )

    def delete(self, contest_id: str) -> None:
        return self.sqlhandler.execute(
            """
                DELETE FROM contests WHERE contest_id = %s
            """,
            contest_id,
        )
