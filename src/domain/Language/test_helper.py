from datetime import datetime
from typing import List
from domain.Language.language import Language


def create_test_datetime():
    return datetime(2021, 10, 5, 10, 10, 21, 0)


def create_languages(n: int) -> List[Language]:
    result = list()
    for i in range(n):
        result.append(Language(
            language=f"test{i}",
            version=f"{i}.{i}",
            base_image=f"test{i}",
            compile_command=f"test Main.test{i}",
            execute_command="./a.out",
            created_at=create_test_datetime(),
            updated_at=create_test_datetime(),
        ).as_json())
    return result
