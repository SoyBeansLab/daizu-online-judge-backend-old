from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Notification(BaseModel):
    id: str
    description: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def __init__(
        self,
        id: str,
        description: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(
            id=id,
            description=description,
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
