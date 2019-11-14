from domain.User.database.user_repository import UserRepository
from domain.User.usecase.user_interactor import UserInteractor
from domain.User.user import User, UserSchema
from infrastructure.database.postgres.sqlhandler import SqlHandler


class UserController:
    def __init__(self, sqlhandler: SqlHandler):
        self.interactor = UserInteractor(UserRepository(sqlhandler))

    async def create(self, req, resp):
        data = await req.media("json")
        try:
            user = User(data["username"])
        except KeyError:
            resp.status_code = 400
            return

        if self.interactor.create(user):
            resp.status_code = 201
        else:
            resp.status_code = 418

    async def users(self, req, resp):
        """
        ---
        get:
            description: Get all users
            responses:
                200:
                    description: Users to be returned
                    contest:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/User'
        """
        resp.media = {
            "users": [UserSchema().dump(user) for user in self.interactor.users()]
        }
        resp.status_code = 200
