from typing import List

from domain.Submission.usecase.submission_repository import SubmissionRepository
from domain.Submission.submission import Submission


class SubmissionInteractor:
    def __init__(self, repository: SubmissionRepository):
        self.repository = repository

    def submit(self, submission: Submission) -> None:
        return self.repository.store(submission)

    def fetch_submissions(self, problem_id: str) -> List[Submission]:
        return self.repository.find_all(problem_id)

    def fetch_submission(self, submit_id: str) -> Submission:
        return self.repository.find(submit_id)
