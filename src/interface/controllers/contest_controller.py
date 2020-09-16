from logging import getLogger

from domain.Contest.contest import Contest
from domain.Contest.database.contest_repository import ContestRepository
from domain.Contest.usecase.contest_interactor import ContestInteractor

from interface.database.sqlhandler import SqlHandler

from exceptions.database import DuplicateKeyError
from exceptions.waf import DuplicateKeyHTTPException

logger = getLogger("daizu").getChild("LanguageController")


class ContestController:
    def __init__(self, sqlhandler: SqlHandler, fastapi):
        self.interactor = ContestInteractor(ContestRepository(sqlhandler))
        self.HTTPException = fastapi.HTTPException

    async def contests(self):
        recent_contests = []
        upcoming_contests = []
        current_contests = []
        resp = dict()

        for contest in self.interactor.recent_contests():
            recent_contests.append(contest.as_json())
        for contest in self.interactor.upcoming_contests():
            upcoming_contests.append(contest.as_json())
        for contest in self.interactor.current_contests():
            current_contests.append(contest.as_json())

        resp["data"] = {
            "upcoming": upcoming_contests,
            "current": current_contests,
            "recent": recent_contests,
        }
        resp["status"] = "Success"

        return resp

    async def contest(self, contest_id: str):
        resp = dict()
        contest = self.interactor.contest(contest_id)
        if contest is None:
            raise self.HTTPException(
                status_code=404, detail="contest not found"
            )
        resp["data"] = contest.as_json()
        resp["status"] = "Success"

        return resp

    async def store(self, contest: Contest):
        resp = dict()
        contest_id = contest.contest_id

        # The contest_id is determined by the admin so make sure there are no duplicates.
        try:
            self.interactor.store(contest)
            resp["status"] = "Success"
            resp["message"] = "Create contest"
        except DuplicateKeyError as e:
            message = f"Duplicate key (Key: {contest_id})"
            logger.debug(message, e)
            raise DuplicateKeyHTTPException(detail=message)

        return resp

    async def update(self, contest_id: str, contest: Contest):
        resp = {
            "status": "Success",
            "message": "Update contest",
        }
        self.interactor.update(contest_id, contest)

        return resp

    async def delete(self, contest_id: str):
        resp = {
            "status": "Success",
            "message": f"Delete contest (contest_id={contest_id})",
        }
        self.interactor.delete(contest_id)

        return resp
