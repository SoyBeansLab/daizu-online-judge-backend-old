from typing import List

from domain.Registration.usecase.registration_repository import (
    RegistrationRepository,
)
from domain.Registration.registration import Registration


class RegistrationInteractor:
    def __init__(self, repository: RegistrationRepository):
        self.repository = repository

    def registrations(self) -> List[Registration]:
        return self.repository.find_all()

    def registration(self) -> Registration:
        return self.repository.find()
