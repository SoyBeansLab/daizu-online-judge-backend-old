from domain.Language.database.language_repository import LanguageRepository
from domain.Language.usecase.language_interactor import LanguageInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class LanguageController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = LanguageInteractor(LanguageRepository(sqlhandler))

    async def languages(self, req, resp):
        languages = []
        for lang in self.interactor.languages():
            languages.append(lang.language)
        resp.media = {
            "data": languages
        }
        resp.status_code = 200
