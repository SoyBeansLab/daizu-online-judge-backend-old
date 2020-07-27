from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, ValidationError, validator


class Submission(BaseModel):
    submit_id: str
    username: str
    problem_id: str
    result: str
    language: str
    score: int
    test_case: str
    source_code: str
    code_size: int
    compile_message: str
    created_at: Optional[datetime]

    def __init__(
        self,
        submit_id: str,
        username: str,
        problem_id: str,
        result: str,
        language: str,
        score: int,
        test_case: str,
        source_code: str,
        code_size: int,
        compile_message: str,
        created_at: Optional[datetime],
    ):
        super().__init__(
            submit_id=submit_id
            if submit_id is not None
            else self.__generate_id(),
            username=username,
            problem_id=problem_id,
            result=result,
            language=language,
            score=score,
            test_case=test_case,
            source_code=source_code,
            code_size=code_size,
            compile_message=compile_message,
            created_at=created_at,
        )

    def __generate_id(self):
        return str(uuid.uuid4())

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["submit_date"] = str(d["submit_date"])
        return d
