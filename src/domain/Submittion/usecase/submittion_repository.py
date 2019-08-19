from abc import ABC, abstractmethod
from typing import List

from domain.Submittion.submittion import Submittion


class SubmittionRepository(ABC):
    @abstractmethod
    def store(self, submittion: Submittion) -> int:
        pass

    @abstractmethod
    def find_all(self, problem_id: str) -> List[Submittion]:
        pass

    @abstractmethod
    def find(self, submit_id) -> Submittion:
        pass
