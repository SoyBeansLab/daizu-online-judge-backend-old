import responder

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.problem_controller import ProblemController


def set_route(api: responder.API) -> None:
    problem_controller = ProblemController(SqlHandler("problem"))

    api.add_route("/contest/{contest_id}/problems", problem_controller.problems)
    api.add_route(
        "/contest/{contest_id}/problems/{problem_id}",
        problem_controller.problem,
    )
