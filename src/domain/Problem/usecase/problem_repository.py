from abc import ABC, abstractmethod
from typing import List

from domain.Problem.problem import Problem


class ProblemRepository(ABC):
    @abstractmethod
    def find_all(self, contest_id: str) -> List[Problem]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, problem_id: str) -> Problem:
        raise NotImplementedError()
