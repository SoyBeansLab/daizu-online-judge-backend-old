from domain.Submission.database.submission_repotisory import (
    SubmissionRepository,
)
from domain.Submission.submission import Submission
from domain.Submission.usecase.submission_interactor import SubmissionInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class SubmissionController:
    def __init__(self, sqlhandler: SqlHandler, fastapi):
        self.interactor = SubmissionInteractor(SubmissionRepository(sqlhandler))
        self.HTTPException = fastapi.HTTPException

    async def submit(self, contest_id: str, problem_id: str):
        data = await req.media("json")
        try:
            submission = Submission(
                username=data["username"],
                problem_id=problem_id,
                language=data["language"],
                test_case=data["test_case"],
                source_code=data["source_code"],
            )
            resp.media = submission.as_json()
            resp.media = submission.as_json()
            self.interactor.submit(submission)
            return "Created"
        except KeyError:
            raise HTTPException(status_code=400, detail="Key Error")

    async def submissions(self, contest_id: str, problem_id: str):
        rows = self.interactor.fetch_submissions(problem_id)
        submissions = []
        for row in rows:
            submissions.append(row.as_json())
        resp.media = {"submissions": submissions}
        resp.status_code = 200

    async def submission(
        self, contest_id: str, problem_id: str, submit_id: str
    ):
        submission = self.interactor.fetch_submission(submit_id)
        if submission is None:
            res_data = None
        else:
            res_data = submission.as_json()
        resp.media = {"submission": res_data}
        resp.status_code = 200
