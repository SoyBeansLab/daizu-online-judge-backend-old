from datetime import datetime

from domain.Problem.problem import Problem


class TestProblem:
    def test_create_problem(self):
        # pass
        _ = Problem(
            problem_id="problem1",
            contest_id="contest1",
            problem_order=1,
            problem_name="HelloWorld",
            time_limit=2,
            memory_limit=256,
            score=100,
            problem_detail="# print",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

    def test_as_json(self):
        result = Problem(
            problem_id="problem1",
            contest_id="contest1",
            problem_order=1,
            problem_name="HelloWorld",
            time_limit=2,
            memory_limit=256,
            score=100,
            problem_detail="# print",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )
        want = {
            "problem_id": "problem1",
            "contest_id": "contest1",
            "problem_order": 1,
            "problem_name": "HelloWorld",
            "time_limit": 2,
            "memory_limit": 256,
            "score": 100,
            "problem_detail": "# print",
            "created_at": str(self.gen_test_datetime()),
            "updated_at": str(self.gen_test_datetime()),
        }
        assert result.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
