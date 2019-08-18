import responder

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController


def set_route(api: responder.API) -> None:
    contest_controller = ContestController(SqlHandler("contest"))

    api.add_route("/contests", contest_controller.contests)
    api.add_route("/contest/{contest_id}", contest_controller.contest)
