from dataclasses import dataclass


@dataclass
class User:
    """
    username: str length <= 16
    """
    username: str

    def as_dict(self):
        return self.__dict__