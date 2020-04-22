import datetime
import secrets


class Contest:
    def __init__(
        self,
        contest_id: str,
        contest_name: str,
        contest_start_date: datetime.datetime,
        contest_finish_date: datetime.datetime,
        contest_time: int,
        writer: str,
        contest_description: str,
        problem_number: int,
    ):
        self.contest_id = contest_id
        self.contest_name = contest_name
        self.contest_start_date = contest_start_date
        self.contest_finish_date = contest_finish_date
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
        d["contest_start_date"] = str(d["contest_start_date"])
        d["contest_finish_date"] = str(d["contest_finish_date"])
        return d
