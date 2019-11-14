from abc import ABC, abstractmethod
from typing import List

from domain.Submittion.submittion import Submittion


class SubmittionRepository(ABC):
    @abstractmethod
    def store(self, submittion: Submittion) -> int:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, problem_id: str) -> List[Submittion]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, submit_id) -> Submittion:
        raise NotImplementedError()
