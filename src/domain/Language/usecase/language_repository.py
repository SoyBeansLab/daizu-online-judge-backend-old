from abc import ABC, abstractclassmethod
from typing import List

from domain.Language.language import Language


class LanguageRepository(ABC):
    @abstractclassmethod
    def find_all(self) -> List[Language]:
        pass

    @abstractclassmethod
    def store(self, language: Language) -> None:
        pass
