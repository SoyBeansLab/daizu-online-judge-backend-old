from datetime import datetime
import secrets
from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class Contest(BaseModel):
    contest_id: str
    contest_name: str
    contest_start_date: Optional[datetime]
    contest_finish_date: Optional[datetime]
    contest_time: int = None
    writer: str
    description: str = None
    top_content: str
    problem_number: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def __init__(
        self,
        contest_id: str,
        contest_name: str,
        contest_start_date: Optional[datetime],
        contest_finish_date: Optional[datetime],
        contest_time: int,
        writer: str,
        description: str,
        top_content: str,
        problem_number: int,
        created_at: Optional[datetime],
        updated_at: Optional[datetime],
    ):
        super().__init__(
            contest_id = contest_id,
            contest_name = contest_name,
            contest_start_date = contest_start_date,
            contest_finish_date = contest_finish_date,
            contest_time = contest_time,
            writer = writer,
            description = description,
            top_content = top_content,
            problem_number = problem_number,
            created_at = created_at,
            updated_at = updated_at,
        )

    @staticmethod
    def __generate_id(self):
        return secrets.token_hex(4)

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["contest_start_date"] = str(d["contest_start_date"])
        d["contest_finish_date"] = str(d["contest_finish_date"])
        d["created_at"] = str(d["created_at"])
        d["updated_at"] = str(d["updated_at"])
        return d
