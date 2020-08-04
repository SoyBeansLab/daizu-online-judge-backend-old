from abc import ABC, abstractclassmethod
from typing import List

from domain.Notification.notification import Notification


class NotificationRepository(ABC):
    @abstractclassmethod
    def find_all(self) -> List[Notification]:
        pass
