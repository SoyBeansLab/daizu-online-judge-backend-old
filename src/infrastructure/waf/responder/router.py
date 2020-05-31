import responder

from domain.User.user import UserSchema

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController
from interface.controllers.problem_controller import ProblemController
from interface.controllers.submittion_controller import SubmittionController
from interface.controllers.user_controller import UserController
from interface.controllers.language_controller import LanguageController


def set_route(api: responder.API) -> None:
    set_route_contest(api)
    set_route_problem(api)
    set_route_submittion(api)
    set_route_user(api)
    set_route_language(api)


def set_schema(api: responder.API) -> None:
    #    api.add_schema("User", UserSchema)
    pass


def set_route_contest(api: responder.API) -> None:
    contest_controller = ContestController(SqlHandler())

    api.add_route("/contests", contest_controller.contests)
    api.add_route("/contests/{contest_id}", contest_controller.contest)


def set_route_problem(api: responder.API) -> None:
    problem_controller = ProblemController(SqlHandler())

    api.add_route(
        "/contests/{contest_id}/problems", problem_controller.problems
    )
    api.add_route(
        "/contests/{contest_id}/problems/{problem_id}",
        problem_controller.problem,
    )


def set_route_user(api: responder.API) -> None:
    user_controller = UserController(SqlHandler())

    api.add_route("/users/create", user_controller.create)
    api.add_route("/users", user_controller.users)


def set_route_submittion(api: responder.API) -> None:
    submittion_controller = SubmittionController(SqlHandler())

    api.add_route(
        "/contests/{contest_id}/problems/{problem_id}/submit",
        submittion_controller.submit,
    )
    # contest_idで紐づいたそのコンテストの提出リストとかほしい
    api.add_route(
        "/contests/{contest_id}/submittions/{problem_id}",
        submittion_controller.submittions,
    )
    api.add_route(
        "/contests/{contest_id}/submittions/{problem_id}/{submit_id}",
        submittion_controller.submittion,
    )


def set_route_language(api: responder.API) -> None:
    language_controller = LanguageController(SqlHandler())
    api.add_route("/languages", language_controller.languages)
