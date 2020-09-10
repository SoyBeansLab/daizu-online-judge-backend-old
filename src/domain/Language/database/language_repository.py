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
            language.execute_command
        )
