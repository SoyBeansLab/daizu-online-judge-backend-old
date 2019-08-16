from typing import List
from domain.User.user import User
from domain.User.usecase.user_repository import UserRepository


class UserInteractor:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, user: User) -> None:
        return self.repository.store(user)

    def users(self) -> List[User]:
        return self.repository.find_all()
