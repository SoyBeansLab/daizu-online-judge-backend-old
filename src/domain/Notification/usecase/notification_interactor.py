from typing import List

from domain.Notification.usecase.notification_repository import (
    NotificationRepository,
)
from domain.Notification.notification import Notification


class NotificationInteractor:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository

    def notifications(self) -> List[Notification]:
        return self.repository.find_all()

    def store(self, notification: Notification) -> None:
        return self.repository.store(notification)

    def update(self, notification: Notification) -> None:
        return self.repository.update(notification)

    def delete(self, _id: str) -> None:
        return self.repository.delete(_id)
