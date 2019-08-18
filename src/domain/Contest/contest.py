import datetime
import secrets


class Contest:
    def __init__(
        self,
        contest_id: str,
        contest_name: str,
        contest_date: datetime.datetime,
        contest_time: int,
        writer: str,
        contest_description: str,
        problem_number: int,
    ):
        self.contest_id = contest_id
        self.contest_name = contest_name
        self.contest_date = contest_date
        self.contest_time = contest_time
        self.writer = writer
        self.contest_description = contest_description
        self.problem_number = problem_number

    @staticmethod
    def __generate_id(self):
        return secrets.token_hex(4)

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["contest_date"] = str(d["contest_date"])
        return d
