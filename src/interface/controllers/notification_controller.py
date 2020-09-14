from domain.Notification.notification import Notification
from domain.Notification.database.notification_repository import (
    NotificationRepository,
)
from domain.Notification.usecase.notification_interactor import (
    NotificationInteractor,
)
from infrastructure.database.postgres.sqlhandler import SqlHandler


class NotificationController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = NotificationInteractor(
            NotificationRepository(sqlhandler)
        )

    async def notifications(self):
        notifications = []
        for notification in self.interactor.notifications():
            notifications.append(notification.as_json())

        resp = {"notifications": notifications}

        return resp

    async def create(self, notification: Notification):
        self.interactor.store(notification)
        resp = {}
        return resp

    async def update(self, notification: Notification):
        self.interactor.update(notification)
        resp = {}
        return resp

    async def delete(self, id: str):
        self.interactor.delete(id)
        resp = {}

        return resp
