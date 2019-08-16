from abc import ABC, abstractmethod
from typing import List
from domain.User.user import User


class UserRepository(ABC):
    @abstractmethod
    def store(self, user: User) -> int:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find(self, username: str) -> List[User]:
        pass
