import fastapi
from fastapi import FastAPI, status
from starlette.requests import Request

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController
from interface.controllers.problem_controller import ProblemController
from interface.controllers.submittion_controller import SubmittionController
from interface.controllers.user_controller import UserController
from interface.controllers.language_controller import LanguageController
from interface.controllers.registration_controller import RegistrationController


def set_route(api: FastAPI) -> None:
    set_route_contest(api)
    set_route_problem(api)
    set_route_submittion(api)
    #    set_route_user(api)
    set_route_language(api)
    set_router_registration(api)


def set_route_contest(api: FastAPI) -> None:
    contest_controller = ContestController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests",
        contest_controller.contests,
        methods=["GET"],
        status_code=200,
    )
    api.add_api_route(
        "/contests/{contest_id}", contest_controller.contest, methods=["GET"]
    )


def set_route_problem(api: FastAPI) -> None:
    problem_controller = ProblemController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests/{contest_id}/problems",
        problem_controller.problems,
        methods=["GET"],
        status_code=200,
    )
    api.add_api_route(
        "/contests/{contest_id}/problems/{problem_id}",
        problem_controller.problem,
        methods=["GET"],
        status_code=200,
    )


def set_route_user(api: FastAPI) -> None:
    user_controller = UserController(SqlHandler())

    api.add_api_route("/users/create", user_controller.create)
    api.add_api_route("/users", user_controller.users)


def set_route_submittion(api: FastAPI) -> None:
    submittion_controller = SubmittionController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests/{contest_id}/problems/{problem_id}/submit",
        submittion_controller.submit,
        methods=["POST"],
        status_code=201,
    )
    # contest_idで紐づいたそのコンテストの提出リストとかほしい
    api.add_api_route(
        "/contests/{contest_id}/submittions/{problem_id}",
        submittion_controller.submittions,
        methods=["GET"],
        status_code=200,
    )
    api.add_api_route(
        "/contests/{contest_id}/submittions/{problem_id}/{submit_id}",
        submittion_controller.submittion,
        methods=["GET"],
        status_code=200,
    )


def set_route_language(api: FastAPI) -> None:
    language_controller = LanguageController(SqlHandler())
    api.add_api_route(
        "/languages",
        language_controller.languages,
        methods=["GET"],
        status_code=200,
    )


def set_router_registration(api: FastAPI) -> None:
    registration_controller = RegistrationController(SqlHandler())

    api.add_api_route(
        "/registration", registration_controller.registrations, methods=["GET"]
    )
    api.add_api_route(
        "/registration", registration_controller.registration, methods=["POST"]
    )
