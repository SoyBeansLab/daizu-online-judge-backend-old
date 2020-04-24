from domain.Submittion.database.submittion_repotisory import (
    SubmittionRepository,
)
from domain.Submittion.submittion import Submittion
from domain.Submittion.usecase.submittion_interactor import SubmittionInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class SubmittionController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = SubmittionInteractor(SubmittionRepository(sqlhandler))

    async def submit(self, req, resp, *, contest_id, problem_id):
        data = await req.media("json")
        try:
            submittion = Submittion(
                username=data["username"],
                problem_id=problem_id,
                language=data["language"],
                test_case=data["test_case"],
                source_code=data["source_code"],
            )
            resp.media = {
                "data": submittion.as_json()
            }
            self.interactor.submit(submittion)
            resp.status_code = 201
        except KeyError:
            resp.media = data
            resp.status_code = 400

    async def submittions(self, req, resp, *, contest_id, problem_id):
        rows = self.interactor.fetch_submittions(problem_id)
        submittions = []
        for row in rows:
            submittions.append(row.as_json())
        resp.media = {
            "data": submittions
        }
        resp.status_code = 200

    async def submittion(self, req, resp, *, contest_id, problem_id, submit_id):
        submittion = self.interactor.fetch_submittion(submit_id)
        if submittion is None:
            res_data = None
        else:
            res_data = submittion.as_json()
        resp.media = {
            "data": res_data
        }
        resp.status_code = 200
