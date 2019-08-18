import datetime
import secrets


class Contest:
    def __init__(
            self,
            contest_name: str,
            contest_date: datetime.datetime,
            contest_time: int,
            writer: str,
            contest_description: str,
            problem_number: int,
            ):
        self.contest_id = self.__generate_id()
        self.contest_name = contest_name
        self.contest_date = contest_date
        self.contest_time = contest_time
        self.writer = writer
        self.contest_description = contest_description
        self.problem_number = problem_number

    @staticmethod
    def __generate_id(self):
        return secrets.token_hex(4)

    def to_dict(self):
        return self.__dict__

