from typing import List

from domain.Problem.usecase.problem_repository import ProblemRepository
from domain.Problem.problem import Problem


class ProblemInteracor:
    def __init__(self, repository: ProblemRepository):
        self.repository = repository

    def problem(self, problem_id: str) -> Problem:
        return self.repository.find(problem_id)

    def problems(self, contest_id: str) -> List[Problem]:
        return self.repository.find_all(contest_id)
