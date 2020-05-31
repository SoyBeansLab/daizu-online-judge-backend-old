from typing import List
from datetime import datetime

from domain.Registration.usecase.registration_repository import (
    RegistrationRepository as AbsRegistrationRepository,
)
from domain.Registration.registration import Registration
from infrastructure.database.postgres.sqlhandler import SqlHandler


class RegistrationRepository(AbsRegistrationRepository):
    def __init__(self, sqlhandler: SqlHandler):
        self.sqlhandler = sqlhandler

    def find_all(self) -> List[Registration]:
        query = "SELECT * FROM registrations"
        rows = self.sqlhandler.query(query).fetch_all()
        return [Registration(*row) for row in rows]

    def find(self, contest_id: str, username: str):
        query = "SELECT * FROM registration WHERE contest_id = %s AND username = %s"
        row = self.sqlhandler.query(query).fetch_one()

        if not row:
            return None
        return Registration(*row)
