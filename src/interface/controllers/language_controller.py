from logging import getLogger

from domain.Language.language import Language
from domain.Language.database.language_repository import LanguageRepository
from domain.Language.usecase.language_interactor import LanguageInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler

from exceptions.database import DuplicateKeyError
from exceptions.waf import DuplicateKeyHTTPException

logger = getLogger("daizu").getChild("LanguageController")


class LanguageController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = LanguageInteractor(LanguageRepository(sqlhandler))

    async def languages(self):
        languages = []
        resp = dict()
        for lang in self.interactor.languages():
            languages.append(lang)
        resp["data"] = languages
        resp["status"] = "Success"

        return resp

    async def create_language(self, language: Language):
        resp = dict()
        language_name = language.language
        try:
            self.interactor.store(language)
            resp["status"] = "Success"
            resp["message"] = "Create language"
        except DuplicateKeyError as e:
            message = f"Duplicate key. (Key: {language_name})"
            logger.debug(message, e)
            raise DuplicateKeyHTTPException(detail=message)

        return resp

    async def update(self, language: Language):
        resp = {
            "status": "Success",
            "message": "Update language",
        }
        self.interactor.update(language)

        return resp

    async def delete(self, language_name: str):
        resp = {
            "status": "Success",
            "message": f"Delete language.(language={language_name})",
        }
        self.interactor.delete(language_name)

        return resp
