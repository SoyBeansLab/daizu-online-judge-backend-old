from domain.Problem.database.problem_repository import ProblemRepository
from domain.Problem.usecase.problem_interactor import ProblemInteracor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ProblemController:
    def __init__(self, sqlhandler: SqlHandler, fastapi):
        self.interactor = ProblemInteracor(ProblemRepository(sqlhandler))
        self.HTTPException = fastapi.HTTPException

    async def problems(self, contest_id: str):
        problems = []
        for problem in self.interactor.problems(contest_id):
            problems.append(problem.as_json())
        resp = {"problems": problems}
        return resp

    async def problem(self, contest_id: str, problem_id: str):
        problem = self.interactor.problem(problem_id)
        if problem is None:
            raise self.HTTPException(
                status_code=404, detail="problem not found"
            )

        res_data = problem.as_json()
        resp = {"problem": res_data}
        return resp
