from abc import ABC, abstractmethod


class Result(ABC):
    @abstractmethod
    def lastrowsid(self) -> int:
        raise NotImplementedError()


class Cursor(ABC):
    @abstractmethod
    def fetch_all(self):
        raise NotImplementedError()

    @abstractmethod
    def fetch_one(self):
        raise NotImplementedError()


class SqlHandler(ABC):
    @abstractmethod
    def execute(self, query: str, *args) -> Result:
        raise NotImplementedError()

    @abstractmethod
    def query(self, sql: str, *args) -> Cursor:
        raise NotImplementedError()
