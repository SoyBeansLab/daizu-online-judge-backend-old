from domain.Contest.database.contest_repository import ContestRepository
from domain.Contest.usecase.contest_interactor import ContestInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ContestController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = ContestInteractor(ContestRepository(sqlhandler))

    async def contests(self, req, resp):
        contests = []
        for contest in self.interactor.contests():
            contests.append(contest.as_json())
        resp.media = {"contests": contests}
        resp.status_code = 200

    async def contest(self, req, resp, *, contest_id):
        contest = self.interactor.contest(contest_id)
        resp.media = {"contest": contest.as_json()}
        resp.status_code = 200
