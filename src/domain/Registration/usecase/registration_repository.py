from abc import ABC, abstractmethod
from typing import List

from domain.Registration.registration import Registration


class RegistrationRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Registration]:
        raise NotImplementedError()

    @abstractmethod
    def find(self, contest_id: str, username: str) -> Registration:
        raise NotImplementedError()
