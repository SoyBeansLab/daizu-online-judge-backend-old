from datetime import datetime
import pytest
from pytest_mock import MockFixture

from domain.Contest.contest import Contest


class TestContest:
    def test_create_contest(self):
        # pass
        # compile_command can be empty
        Contest(
            contest_id="test0001",
            contest_name="HelloWorld",
            contest_start_date=self.gen_test_datetime(),
            contest_finish_date=self.gen_test_datetime(),
            contest_time=256,
            writer="ucpr",
            description="test",
            top_content="test",
            problem_number=4,
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

    def test_to_json(self):
        result = Contest(
            contest_id="test0001",
            contest_name="HelloWorld",
            contest_start_date=self.gen_test_datetime(),
            contest_finish_date=self.gen_test_datetime(),
            contest_time=256,
            writer="ucpr",
            description="test",
            top_content="test",
            problem_number=4,
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )
        want = {
            "contest_id": "test0001",
            "contest_name": "HelloWorld",
            "contest_start_date": str(self.gen_test_datetime()),
            "contest_finish_date": str(self.gen_test_datetime()),
            "contest_time": 256,
            "writer": "ucpr",
            "description": "test",
            "top_content": "test",
            "problem_number": 4,
            "created_at": str(self.gen_test_datetime()),
            "updated_at": str(self.gen_test_datetime()),
        }
        assert result.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
