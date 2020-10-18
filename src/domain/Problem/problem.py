from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class Problem(BaseModel):
    problem_id: str
    contest_id: str
    problem_order: int
    problem_name: str
    time_limit: int
    memory_limit: int
    score: int
    problem_detail: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def __init__(
        self,
        problem_id: str,
        contest_id: str,
        problem_order: int,
        problem_name: str,
        time_limit: int,
        memory_limit: int,
        score: int,
        problem_detail: str,
        created_at: Optional[datetime],
        updated_at: Optional[datetime],
    ):
        super().__init__(
            contest_id=contest_id,
            problem_id=problem_id,
            problem_order=problem_order,
            problem_name=problem_name,
            time_limit=time_limit,
            memory_limit=memory_limit,
            score=score,
            problem_detail=problem_detail,
            created_at=created_at,
            updated_at=updated_at,
        )

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["created_at"] = str(d["created_at"])
        d["updated_at"] = str(d["updated_at"])
        return d
