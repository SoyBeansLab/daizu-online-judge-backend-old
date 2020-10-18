from datetime import datetime

from domain.Registration.registration import Registration


class TestRegistration:
    def test_create_registration(self):
        _ = Registration(
            contest_id="contest1",
            username="ucpr",
            created_at=self.gen_test_datetime(),
        )

    def test_as_json(self):
        result = Registration(
            contest_id="contest1",
            username="ucpr",
            created_at=self.gen_test_datetime(),
        )
        want = {
            "contest_id": "contest1",
            "username": "ucpr",
            "created_at": str(self.gen_test_datetime()),
        }
        assert result.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
