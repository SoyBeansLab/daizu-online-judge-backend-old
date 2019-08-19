from typing import List

from domain.Submittion.usecase.submittion_repository import SubmittionRepository
from domain.Submittion.submittion import Submittion


class SubmittionInteractor:
    def __init__(self, repository: SubmittionRepository):
        self.repository = repository

    def submit(self, submittion: Submittion) -> None:
        return self.repository.store(submittion)

    def fetch_submittions(self, problem_id: str) -> List[Submittion]:
        return self.repository.find_all(problem_id)

    def fetch_submittion(self, submit_id: str) -> Submittion:
        return self.repository.find(submit_id)
