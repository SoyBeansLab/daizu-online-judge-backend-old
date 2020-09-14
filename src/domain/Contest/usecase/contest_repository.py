from abc import ABC, abstractmethod
from typing import List

from domain.Contest.contest import Contest


class ContestRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Contest]:
        raise NotImplementedError()

    @abstractmethod
    def find_upcoming(self) -> List[Contest]:
        raise NotImplementedError()

    @abstractmethod
    def find_current(self) -> List[Contest]:
        raise NotImplementedError()

    @abstractmethod
    def find_recent(self) -> List[Contest]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, contest_id: str) -> Contest:
        raise NotImplementedError()

    @abstractmethod
    def store(self, contest: Contest) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, contest_id: str, contest: Contest) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, contest_id: str) -> None:
        raise NotImplementedError
