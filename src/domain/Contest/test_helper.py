from datetime import datetime, timedelta
from typing import List
from domain.Contest.contest import Contest


def create_test_datetime() -> datetime:
    return datetime(2021, 10, 5, 10, 10, 21, 0)


def create_recent_test_datetime() -> datetime:
    """ Based on 2025-01-01 00:00:00 """
    return datetime(2024, 1, 1, 0, 0, 0, 0)


def create_upcoming_test_datetime() -> datetime:
    """ Based on 2025-01-01 00:00:00 """
    return datetime(2024, 1, 1, 0, 0, 0, 0)


def create_current_test_datetime() -> datetime:
    """ Based on 2025-01-01 00:00:00 """
    return datetime(2025, 1, 1, 0, 10, 0, 0)


def create_recent_contests(n: int) -> List[Contest]:
    result = list()
    for i in range(n):
        result.append(
            Contest(
                contest_id=f"test_recent_{i}",
                contest_name="TestRecentContest{i}",
                contest_start_date=create_recent_test_datetime(),
                contest_finish_date=create_recent_test_datetime()
                + timedelta(days=1),
                contest_time=120,
                writer="ucpr",
                description="Welcome",
                top_content="Welcome",
                problem_number=4,
                created_at=create_test_datetime(),
                updated_at=create_test_datetime(),
            ).as_json()
        )
    return result


def create_upcoming_contests(n: int) -> List[Contest]:
    result = list()
    for i in range(n):
        result.append(
            Contest(
                contest_id=f"test_upcoming_{i}",
                contest_name="TestUpcomingContest{i}",
                contest_start_date=create_upcoming_test_datetime(),
                contest_finish_date=create_upcoming_test_datetime()
                + timedelta(days=1),
                contest_time=120,
                writer="ucpr",
                description="Welcome",
                top_content="Welcome",
                problem_number=4,
                created_at=create_test_datetime(),
                updated_at=create_test_datetime(),
            ).as_json()
        )
    return result


def create_current_contests(n: int) -> List[Contest]:
    result = list()
    for i in range(n):
        result.append(
            Contest(
                contest_id=f"test_current_{i}",
                contest_name="TestCurrentContest{i}",
                contest_start_date=create_current_test_datetime(),
                contest_finish_date=create_current_test_datetime()
                + timedelta(days=1),
                contest_time=120,
                writer="ucpr",
                description="Welcome",
                top_content="Welcome",
                problem_number=4,
                created_at=create_test_datetime(),
                updated_at=create_test_datetime(),
            ).as_json()
        )
    return result
