import responder

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController
from interface.controllers.problem_controller import ProblemController


def set_route(api: responder.API) -> None:
    set_route_contest(api)
    set_route_problem(api)


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
