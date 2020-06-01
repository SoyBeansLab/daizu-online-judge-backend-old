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

    async def registrations(self, req, resp):
        registrations = []

        for registration in self.interactor.registrations():
            registrations.append(registration.as_json())

        resp.media = registrations
        resp.status_code = 200

    async def registration(self, req, res):
        pass
