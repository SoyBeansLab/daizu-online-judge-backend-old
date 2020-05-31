from datetime import datetime


class Registration:
    def __init__(
        self,
        contest_id: str,
        username: str,
        created_at: datetime,
    ):
        self.contest_id = contest_id
        self.username = username
        self.created_at = created_at

    def as_dict(self):
        return self.__dict__

    def as_json(self):
        d = self.as_dict()
        d["created_at"] = str(d["created_at"])
        return d
