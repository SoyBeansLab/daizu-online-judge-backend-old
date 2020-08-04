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
        created_at: Optional[datetime],
        updated_at: Optional[datetime],
    ):
        super().__init__(
            id=id,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )
