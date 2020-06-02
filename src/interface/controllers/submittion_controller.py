from domain.Submittion.database.submittion_repotisory import (
    SubmittionRepository,
)
from domain.Submittion.submittion import Submittion
from domain.Submittion.usecase.submittion_interactor import SubmittionInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class SubmittionController:
    def __init__(self, sqlhandler: SqlHandler, fastapi):
        self.interactor = SubmittionInteractor(SubmittionRepository(sqlhandler))
        self.HTTPException = fastapi.HTTPException

    async def submit(self, contest_id: str, problem_id: str):
        data = await req.media("json")
        try:
            submittion = Submittion(
                username=data["username"],
                problem_id=problem_id,
                language=data["language"],
                test_case=data["test_case"],
                source_code=data["source_code"],
            )
            resp.media = submittion.as_json()
            resp.media = submittion.as_json()
            self.interactor.submit(submittion)
            return "Created"
        except KeyError:
            raise HTTPException(status_code=400, detail="Key Error")

    async def submittions(self, contest_id: str, problem_id: str):
        rows = self.interactor.fetch_submittions(problem_id)
        submittions = []
        for row in rows:
            submittions.append(row.as_json())
        resp.media = {"submittions": submittions}
        resp.status_code = 200

    async def submittion(
        self, contest_id: str, problem_id: str, submit_id: str
    ):
        submittion = self.interactor.fetch_submittion(submit_id)
        if submittion is None:
            res_data = None
        else:
            res_data = submittion.as_json()
        resp.media = {"submittion": res_data}
        resp.status_code = 200
