from datetime import datetime
import pytest

from domain.Notification.notification import Notification


class TestNotification:
    def test_create_notification(self):
        # pass
        _ = Notification(
            id="notif_id",
            description="description",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

    def test_to_json(self):
        result = Notification(
            id="notif_id",
            description="description",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )
        want = {
            "id": "notif_id",
            "description": "description",
            "created_at": str(self.gen_test_datetime()),
            "updated_at": str(self.gen_test_datetime()),
        }
        assert result.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
