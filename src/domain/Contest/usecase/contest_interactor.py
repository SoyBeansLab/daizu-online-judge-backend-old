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

    def upcoming_contests(self) -> List[Contest]:
        return self.repository.find_upcoming()

    def current_contests(self) -> List[Contest]:
        return self.repository.find_current()

    def recent_contests(self) -> List[Contest]:
        return self.repository.find_recent()

    def store(self, contest: Contest) -> None:
        return self.repository.store(contest)

    def update(self, contest_id: str, contest: Contest) -> None:
        return self.repository.update(contest_id, contest)

    def delete(self, contest_id: str) -> None:
        return self.repository.delete(contest_id)
