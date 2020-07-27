from abc import ABC, abstractmethod
from typing import List

from domain.Submission.submission import Submission


class SubmissionRepository(ABC):
    @abstractmethod
    def store(self, submission: Submission) -> int:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, problem_id: str) -> List[Submission]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, submit_id) -> Submission:
        raise NotImplementedError()
