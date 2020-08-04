from typing import List

from domain.Notification.usecase.notification_repository import NotificationRepository
from domain.Notification.notification import Notification


class NotificationInteractor:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def notifications(self) -> List[Notification]:
        return self.repository.find_all()
