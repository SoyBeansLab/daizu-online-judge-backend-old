from typing import List

from domain.Notification.usecase.notification_repository import (
    NotificationRepository as AbsNotificationRepository,
)
from domain.Notification.notification import Notification
from infrastructure.database.postgres.sqlhandler import SqlHandler


class NotificationRepository(AbsNotificationRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self) -> List[Notification]:
        rows = self.sqlhandler.query("SELECT * FROM notifications").fetch_all()
        return [Notification(*row) for row in rows]
