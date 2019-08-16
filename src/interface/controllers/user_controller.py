from domain.User.usecase.user_interactor import UserInteractor
from domain.User.database.user_repository import UserRepository
from domain.User.user import User
from infrastructure.database.postgres.sqlhandler import SqlHandler


class UserController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = UserInteractor(UserRepository(sqlhandler))

    async def create(self, req, resp):
        data = await req.media("json")
        user = User(data["username"])
        if self.interactor.create(user):
            resp.status_code = 201
        else:
            resp.status_code = 418

    async def users(self, req, resp):
        resp.media = {
                "users": [user.as_dict() for user in self.interactor.users()]
        }
        resp.status_code = 200
