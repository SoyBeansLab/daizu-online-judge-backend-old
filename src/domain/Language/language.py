from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator


class Language(BaseModel):
    language: str
    version: str
    base_image: str
    compile_command: str
    execute_command: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def __init__(
        self,
        language: str,
        version: str,
        base_image: str,
        compile_command: str,
        execute_command: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(
            language=language,
            version=version,
            base_image=base_image,
            compile_command=compile_command,
            execute_command=execute_command,
            created_at=created_at,
            updated_at=updated_at,
        )

    @validator("language", "version", "base_image", "execute_command")
    def check_empty_str(cls, v):
        """
            compile_commandはスクリプト言語では必要ないのでemptyを許容する.
        """
        if not v:
            raise ValueError("Cannot be empty")
        return v

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["created_at"] = str(d["created_at"])
        d["updated_at"] = str(d["updated_at"])
        return d
