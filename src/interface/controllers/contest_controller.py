from domain.Contest.contest import Contest
from domain.Contest.database.contest_repository import ContestRepository
from domain.Contest.usecase.contest_interactor import ContestInteractor

from interface.database.sqlhandler import SqlHandler


class ContestController:
    def __init__(self, sqlhandler: SqlHandler, fastapi):
        self.interactor = ContestInteractor(ContestRepository(sqlhandler))
        self.HTTPException = fastapi.HTTPException

    async def contests(self):
        recent_contests = []
        upcoming_contests = []
        current_contests = []

        for contest in self.interactor.recent_contests():
            recent_contests.append(contest.as_json())
        for contest in self.interactor.upcoming_contests():
            upcoming_contests.append(contest.as_json())
        for contest in self.interactor.current_contests():
            current_contests.append(contest.as_json())

        resp = {
            "upcoming": upcoming_contests,
            "current": current_contests,
            "recent": recent_contests,
        }
        return resp

    async def contest(self, contest_id: str):
        contest = self.interactor.contest(contest_id)
        if contest is None:
            raise self.HTTPException(
                status_code=404, detail="contest not found"
            )

        res_data = contest.as_json()
        resp = {"contest": res_data}
        return resp

    async def store(self, contest: Contest):
        self.interactor.store(contest)
        resp = {}

        return resp

    async def update(self, contest_id: str, contest: Contest):
        self.interactor.update(contest_id, contest)
        resp = {}

        return resp

    async def delete(self, contest_id: str):
        self.interactor.delete(contest_id)
        resp = {}

        return resp
