from datetime import datetime

from domain.Submission.submission import Submission


class TestSubmission:
    def test_create_submission(self):
        _ = Submission(
            submit_id="submission1",
            username="ucpr",
            problem_id="problem1",
            result="AC",
            language="python3",
            score=100,
            test_case="10/10",
            source_code="print('Hello World')",
            code_size=100,
            compile_message="",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

        # If submit_id is none, submit_id is generated automatically
        result = Submission(
            submit_id=None,
            username="ucpr",
            problem_id="problem1",
            result="AC",
            language="python3",
            score=100,
            test_case="10/10",
            source_code="print('Hello World')",
            code_size=100,
            compile_message="",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )
        assert type(result.submit_id) == type("str")

    def test_as_json(self):
        result = Submission(
            submit_id="submission1",
            username="ucpr",
            problem_id="problem1",
            result="AC",
            language="python3",
            score=100,
            test_case="10/10",
            source_code="print('Hello World')",
            code_size=100,
            compile_message="",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )
        want = {
            "submit_id": "submission1",
            "username": "ucpr",
            "problem_id": "problem1",
            "result": "AC",
            "language": "python3",
            "score": 100,
            "test_case": "10/10",
            "source_code": "print('Hello World')",
            "code_size": 100,
            "compile_message": "",
            "created_at": str(self.gen_test_datetime()),
            "updated_at": str(self.gen_test_datetime()),
        }
        assert result.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
