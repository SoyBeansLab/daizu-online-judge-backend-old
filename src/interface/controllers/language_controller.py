from domain.Language.language import Language
from domain.Language.database.language_repository import LanguageRepository
from domain.Language.usecase.language_interactor import LanguageInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class LanguageController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = LanguageInteractor(LanguageRepository(sqlhandler))

    async def languages(self):
        languages = []
        for lang in self.interactor.languages():
            languages.append(lang)
        resp = {"languages": languages}

        return resp

    async def create_language(self, language: Language):
        print(language)
        self.interactor.store(language)
        resp = {"status": "ok"}

        return resp
