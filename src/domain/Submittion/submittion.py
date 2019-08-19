import datetime
import secrets


class Submittion:
    def __init__(
        self,
        submit_id: str = None,
        submit_date: datetime.datetime = None,
        username: str = None,
        problem_id: str = None,
        result: str = None,
        language: str = None,
        score: int = None,
        test_case: str = None,
        source_code: str = None,
        code_size: int = None,
        compile_message: str = None,
    ):
        if submit_id is not None:
            self.submit_id = submit_id
        else:
            self.submit_id = self.__generate_id()
        if submit_date is not None:
            self.submit_date = submit_date
        else:
            self.submit_date = datetime.datetime.now()
        self.username = username
        self.problem_id = problem_id
        self.result = result
        self.language = language
        self.score = score
        self.test_case = test_case
        self.source_code = source_code
        self.code_size = code_size
        self.compile_message = compile_message

    def __generate_id(self):
        return secrets.token_hex(4)

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["submit_date"] = str(d["submit_date"])
        return d
