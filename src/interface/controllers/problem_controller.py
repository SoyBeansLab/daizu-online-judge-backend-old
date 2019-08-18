from domain.Problem.database.problem_repository import ProblemRepository
from domain.Problem.usecase.problem_interactor import ProblemInteracor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ProblemController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = ProblemInteracor(ProblemRepository(sqlhandler))

    async def problems(self, req, resp, *, contest_id):
        problems = []
        for problem in self.interactor.problems(contest_id):
            problems.append(problem.as_dict())
        resp.media = {"problems": problems}
        resp.status_code = 200

    async def problem(self, req, resp, *, contest_id, problem_id):
        problem = self.interactor.problem(problem_id)
        resp.media = {"problem": problem.as_dict()}
        resp.status_code = 200
