from abc import ABC, abstractmethod
from typing import List

from domain.Contest.contest import Contest


class ContestRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Contest]:
        pass

    @abstractmethod
    def find(self, contest_id: str) -> Contest:
        pass
