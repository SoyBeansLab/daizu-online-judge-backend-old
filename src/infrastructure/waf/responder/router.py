import responder

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController
from interface.controllers.problem_controller import ProblemController
from interface.controllers.submittion_controller import SubmittionController
from interface.controllers.user_controller import UserController


def set_route(api: responder.API) -> None:
    set_route_contest(api)
    set_route_problem(api)
    set_route_submittion(api)
    set_route_user(api)


def set_route_contest(api: responder.API) -> None:
    contest_controller = ContestController(SqlHandler("contest"))

    api.add_route("/contests", contest_controller.contests)
    api.add_route("/contest/{contest_id}", contest_controller.contest)


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


def set_route_submittion(api: responder.API) -> None:
    submittion_controller = SubmittionController(SqlHandler("submittion"))

    api.add_route(
        "/contest/{contest_id}/problems/{problem_id}/submit",
        submittion_controller.submit,
    )
    # contest_idで紐づいたそのコンテストの提出リストとかほしい
    api.add_route(
        "/contest/{contest_id}/submittions/{problem_id}",
        submittion_controller.submittions,
    )
    api.add_route(
        "/contest/{contest_id}/submittions/{problem_id}/{submit_id}",
        submittion_controller.submittion,
    )
