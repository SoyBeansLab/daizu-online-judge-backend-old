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
