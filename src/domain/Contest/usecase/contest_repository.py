from abc import ABC, abstractmethod
from typing import List

from domain.Contest.contest import Contest


class ContestRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Contest]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, contest_id: str) -> Contest:
        raise NotImplementedError()
