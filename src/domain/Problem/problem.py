class Problem:
    def __init__(
        self,
        contest_id: str,
        problem_id: str,
        problem_name: str,
        time_limit: int,
        memory_limit: int,
        score: int,
        writer: str,
        problem_detail: str,
    ):

        self.contest_id = contest_id
        self.problem_id = problem_id
        self.problem_name = problem_name
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.score = score
        self.writer = writer
        self.problem_detail = problem_detail

    def as_dict(self):
        return self.__dict__
