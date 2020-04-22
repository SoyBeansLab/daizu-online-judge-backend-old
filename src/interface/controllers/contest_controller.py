from domain.Contest.database.contest_repository import ContestRepository
from domain.Contest.usecase.contest_interactor import ContestInteractor
from infrastructure.database.postgres.sqlhandler import SqlHandler


class ContestController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = ContestInteractor(ContestRepository(sqlhandler))

    async def contests(self, req, resp):
        recent_contests = []
        upcoming_contests = []
        current_contests = []

        for contest in self.interactor.recent_contests():
            recent_contests.append(contest.as_json())
        for contest in self.interactor.upcoming_contests():
            upcoming_contests.append(contest.as_json())
        for contest in self.interactor.current_contests():
            current_contests.append(contest.as_json())

        resp.media = {
            "upcoming": upcoming_contests,
            "current": current_contests,
            "recent": recent_contests,
        }
        resp.status_code = 200

    async def contest(self, req, resp, *, contest_id):
        contest = self.interactor.contest(contest_id)
        if contest is None:
            res_data = None
            res_code = 400
        else:
            res_data = contest.as_json()
            res_code = 200
        resp.media = {"contest": res_data}
        resp.status_code = res_code
