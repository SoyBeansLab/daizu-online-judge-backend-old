from datetime import datetime
import secrets


class Submittion:
    def __init__(
        self,
        submit_id: str = None,
        username: str = None,
        problem_id: str = None,
        result: str = None,
        language: str = None,
        score: int = None,
        test_case: str = None,
        source_code: str = None,
        code_size: int = None,
        compile_message: str = None,
        created_at: datetime = None,
    ):
        if submit_id is not None:
            self.submit_id = submit_id
        else:
            self.submit_id = self.__generate_id()

        self.username = username
        self.problem_id = problem_id
        self.result = result
        self.language = language
        self.score = score
        self.test_case = test_case
        self.source_code = source_code
        self.code_size = code_size
        self.compile_message = compile_message
        self.created_at = created_at

    def __generate_id(self):
        return secrets.token_hex(4)

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["submit_date"] = str(d["submit_date"])
        return d
