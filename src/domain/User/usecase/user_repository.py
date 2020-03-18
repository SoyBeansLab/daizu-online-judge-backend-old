from abc import ABC, abstractmethod
from typing import List

from domain.User.user import User


class UserRepository(ABC):
    @abstractmethod
    def store(self, user: User) -> int:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self) -> List[User]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, username: str) -> List[User]:
        raise NotImplementedError()
