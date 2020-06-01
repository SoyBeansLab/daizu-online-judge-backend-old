from domain.Registration.database.registration_repository import (
    RegistrationRepository,
)
from domain.Registration.usecase.registration_interactor import (
    RegistrationInteractor,
)
from infrastructure.database.postgres.sqlhandler import SqlHandler


class RegistrationController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = RegistrationInteractor(
            RegistrationRepository(sqlhandler)
        )

    async def registrations(self):
        registrations = []

        for registration in self.interactor.registrations():
            registrations.append(registration.as_json())

        resp = registrations
        return resp

    async def registration(self):
        pass
