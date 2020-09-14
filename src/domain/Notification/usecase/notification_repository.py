from abc import ABC, abstractclassmethod
from typing import List

from domain.Notification.notification import Notification


class NotificationRepository(ABC):
    @abstractclassmethod
    def find_all(self) -> List[Notification]:
        pass

    @abstractclassmethod
    def store(self, notification: Notification) -> None:
        pass

    @abstractclassmethod
    def update(self, notification: Notification) -> None:
        pass

    @abstractclassmethod
    def delete(self, _id: str) -> None:
        pass
