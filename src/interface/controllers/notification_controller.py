from domain.Notification.database.notification_repository import NotificationRepository
from domain.Notification.usecase.notification_interactor import NotificationInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class NotificationController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = NotificationInteractor(NotificationRepository(sqlhandler))

    async def notifications(self):
        notifications = []
        for notification in self.interactor.notifications():
            notifications.append(notification.as_json())

        resp = {"notifications": notifications}

        return resp
