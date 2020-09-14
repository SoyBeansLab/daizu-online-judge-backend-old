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

    def store(self, notification: Notification) -> None:
        return self.sqlhandler.execute(
            """
                INSERT INTO notifications (
                    id,
                    description
                )
                VALUES (%s, %s)
            """,
            notification.id,
            notification.description,
        )

    def update(self, notification: Notification) -> None:
        return self.sqlhandler.execute(
            """
                UPDATE notifications SET
                    id = %s,
                    description = %s
                WHERE id = %s
            """,
            notification.id,
            notification.description,
            notification.id,
        )

    def delete(self, _id: str) -> None:
        return self.sqlhandler.execute(
            """
                DELETE FROM notifications WHERE id = %s
            """,
            _id,
        )
