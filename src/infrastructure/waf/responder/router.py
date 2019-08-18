import responder

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.problem_controller import ProblemController
from interface.controllers.user_controller import UserController


def set_route(api: responder.API) -> None:
    set_route_problem(api)
    set_route_user(api)


def set_route_problem(api: responder.API) -> None:
    problem_controller = ProblemController(SqlHandler("problem"))

    api.add_route("/contest/{contest_id}/problems", problem_controller.problems)
    api.add_route(
        "/contest/{contest_id}/problems/{problem_id}",
        problem_controller.problem,
    )


def set_route_user(api: responder.API) -> None:
    user_controller = UserController(SqlHandler("doj_user"))

    api.add_route("/user/create", user_controller.create)
    api.add_route("/users", user_controller.users)