import responder
from interface.controllers.user_controller import UserController
from infrastructure.database.postgres.sqlhandler import SqlHandler


def set_route(api: responder.API) -> None:
    sqlhandler = SqlHandler("doj_user")
    user_controller = UserController(sqlhandler)

    api.add_route("/user/create", user_controller.create)
    api.add_route("/users", user_controller.users)
