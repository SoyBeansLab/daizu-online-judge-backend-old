from abc import ABC, abstractmethod


class Result(ABC):
    @abstractmethod
    def lastrowsid(self) -> int:
        pass


class Cursor(ABC):
    @abstractmethod
    def fetch_all(self):
        pass

    @abstractmethod
    def fetch_one(self):
        pass


class SqlHandler(ABC):
    @abstractmethod
    def execute(self, query: str, *args) -> Result:
        pass

    @abstractmethod
    def query(self, sql: str, *args) -> Cursor:
        pass
