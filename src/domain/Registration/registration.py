from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError, validator


class Registration(BaseModel):
    contest_id: str
    username: str
    created_at: Optional[datetime]

    def __init__(
        self, contest_id: str, username: str, created_at: Optional[datetime],
    ):
        super().__init__(
            contest_id=contest_id, username=username, created_at=created_at,
        )

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["created_at"] = str(d["created_at"])
        return d
