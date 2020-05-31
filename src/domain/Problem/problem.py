from datetime import datetime

class Problem:
    def __init__(
        self,
        problem_id: str,
        contest_id: str,
        problem_order: int,
        problem_name: str,
        time_limit: int,
        memory_limit: int,
        score: int,
        problem_detail: str,
        created_at: datetime,
        updated_at: datetime,
    ):

        self.contest_id = contest_id
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.score = score
        self.problem_detail = problem_detail
        self.created_at = created_at
        self.updated_at = updated_at

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["created_at"] = str(d["created_at"])
        d["updated_at"] = str(d["updated_at"])
        return d
