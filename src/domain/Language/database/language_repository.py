from typing import List

from domain.Language.usecase.language_repository import (
    LanguageRepository as AbsLanguageRespository,
)
from domain.Language.language import Language
from infrastructure.database.postgres.sqlhandler import SqlHandler


class LanguageRepository(AbsLanguageRespository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self) -> List[Language]:
        rows = self.sqlhandler.query("SELECT * FROM languages").fetch_all()
        return [Language(*row) for row in rows]

    def store(self, language: Language) -> None:
        return self.sqlhandler.execute(
            """
                INSERT INTO languages (
                    language,
                    version,
                    base_image,
                    compile_command,
                    execute_command
                )
                VALUES (%s, %s, %s, %s, %s)
            """,
            language.language,
            language.version,
            language.base_image,
            language.compile_command,
            language.execute_command,
        )

    def update(self, language: Language) -> None:
        return self.sqlhandler.execute(
            """
                UPDATE languages SET
                    language = %s,
                    version = %s,
                    base_image = %s,
                    compile_command = %s,
                    execute_command = %s
                WHERE language = %s
            """,
            language.language,
            language.version,
            language.base_image,
            language.compile_command,
            language.execute_command,
            language.language,
        )

    def delete(self, language_name: str) -> None:
        return self.sqlhandler.execute(
            """
                DELETE FROM languages WHERE language = %s
            """,
            language_name,
        )
