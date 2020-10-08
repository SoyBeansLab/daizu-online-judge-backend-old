from datetime import datetime
import pytest
from pytest_mock import MockFixture

from language import Language


class TestLanguage:
    def test_create_language(self):
        # pass
        # compile_command can be empty
        Language(
            language="Python",
            version="3.8.5",
            base_image="python:3.8.5",
            compile_command="",
            execute_command="python Main.py",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

        with pytest.raises(ValueError):
            Language(
                language="",
                version="3.8.5",
                base_image="python:3.8.5",
                compile_command="",
                execute_command="python Main.py",
                created_at=self.gen_test_datetime(),
                updated_at=self.gen_test_datetime(),
            )

    def test_to_json(self):
        lang = Language(
            language="Python",
            version="3.8.5",
            base_image="python:3.8.5",
            compile_command="",
            execute_command="python Main.py",
            created_at=self.gen_test_datetime(),
            updated_at=self.gen_test_datetime(),
        )

        want = {
            "language": "Python",
            "version": "3.8.5",
            "base_image": "python:3.8.5",
            "compile_command": "",
            "execute_command": "python Main.py",
            "created_at": str(self.gen_test_datetime()),
            "updated_at": str(self.gen_test_datetime()),
        }
        assert lang.as_json() == want

    def gen_test_datetime(self):
        return datetime(2020, 10, 5, 10, 10, 21, 0)
