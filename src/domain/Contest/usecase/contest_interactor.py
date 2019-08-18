from typing import List

from domain.Contest.usecase.contest_repository import ContestRepository
from domain.Contest.contest import Contest


class ContestInteractor:
    def __init__(self, repository: ContestRepository):
        self.repository = repository

    def contest(self, contest_id: str) -> Contest:
        return self.repository.find(contest_id)

    def contests(self) -> List[Contest]:
        return self.repository.find_all()
