from typing import List

from domain.Language.usecase.language_repository import LanguageRepository
from domain.Language.language import Language


class LanguageInteractor:
    def __init__(self, repository: LanguageRepository):
        self.repository = repository

    def languages(self) -> List[Language]:
        return self.repository.find_all()

    def store(self, language: Language) -> None:
        return self.repository.store(language)

    def update(self, language: Language) -> None:
        return self.repository.update(language)

    def delete(self, language_name: str) -> None:
        return self.repository.delete(language_name)
