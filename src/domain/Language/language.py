from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError, validator


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
        )
