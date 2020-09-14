import fastapi
from fastapi import FastAPI, status
from starlette.requests import Request

from infrastructure.database.postgres.sqlhandler import SqlHandler
from interface.controllers.contest_controller import ContestController
from interface.controllers.problem_controller import ProblemController
from interface.controllers.submission_controller import SubmissionController
from interface.controllers.user_controller import UserController
from interface.controllers.language_controller import LanguageController
from interface.controllers.registration_controller import RegistrationController
from interface.controllers.notification_controller import NotificationController


def set_route(api: FastAPI) -> None:
    set_route_contest(api)
    set_route_problem(api)
    set_route_submission(api)
    #    set_route_user(api)
    set_route_language(api)
    set_router_registration(api)
    set_route_notification(api)


def set_route_contest(api: FastAPI) -> None:
    contest_controller = ContestController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests",
        contest_controller.contests,
        methods=["GET"],
        status_code=200,
        tags=["contests"],
    )
    api.add_api_route(
        "/contests/{contest_id}",
        contest_controller.contest,
        methods=["GET"],
        tags=["contests"],
    )


def set_route_problem(api: FastAPI) -> None:
    problem_controller = ProblemController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests/{contest_id}/problems",
        problem_controller.problems,
        methods=["GET"],
        status_code=200,
        tags=["problems"],
    )
    api.add_api_route(
        "/contests/{contest_id}/problems/{problem_id}",
        problem_controller.problem,
        methods=["GET"],
        status_code=200,
        tags=["problems"],
    )


def set_route_user(api: FastAPI) -> None:
    user_controller = UserController(SqlHandler())

    api.add_api_route("/users/create", user_controller.create)
    api.add_api_route("/users", user_controller.users)


def set_route_submission(api: FastAPI) -> None:
    submission_controller = SubmissionController(SqlHandler(), fastapi)

    api.add_api_route(
        "/contests/{contest_id}/problems/{problem_id}/submit",
        submission_controller.submit,
        methods=["POST"],
        status_code=201,
        tags=["submissions"],
    )
    # contest_idで紐づいたそのコンテストの提出リストとかほしい
    api.add_api_route(
        "/contests/{contest_id}/submissions/{problem_id}",
        submission_controller.submissions,
        methods=["GET"],
        status_code=200,
        tags=["submissions"],
    )
    api.add_api_route(
        "/contests/{contest_id}/submissions/{problem_id}/{submit_id}",
        submission_controller.submission,
        methods=["GET"],
        status_code=200,
        tags=["submissions"],
    )


def set_route_language(api: FastAPI) -> None:
    language_controller = LanguageController(SqlHandler())
    api.add_api_route(
        "/languages",
        language_controller.languages,
        methods=["GET"],
        status_code=200,
        tags=["languages"],
    )
    api.add_api_route(
        "/languages",
        language_controller.create_language,
        methods=["POST"],
        status_code=201,
        tags=["languages"],
    )
    api.add_api_route(
        "/languages",
        language_controller.update,
        methods=["PUT"],
        status_code=200,
        tags=["languages"],
    )
    api.add_api_route(
        "/languages",
        language_controller.delete,
        methods=["DELETE"],
        status_code=200,
        tags=["languages"],
    )


def set_router_registration(api: FastAPI) -> None:
    registration_controller = RegistrationController(SqlHandler())

    api.add_api_route(
        "/registration",
        registration_controller.registrations,
        methods=["GET"],
        tags=["registrations"],
    )
    api.add_api_route(
        "/registration",
        registration_controller.registration,
        methods=["POST"],
        tags=["registrations"],
    )


def set_route_notification(api: FastAPI) -> None:
    notification_controller = NotificationController(SqlHandler())

    api.add_api_route(
        "/notifications",
        notification_controller.notifications,
        methods=["GET"],
        tags=["notifications"],
    )
    api.add_api_route(
        "/notifications",
        notification_controller.create,
        methods=["POST"],
        tags=["notifications"],
    )
    api.add_api_route(
        "/notifications",
        notification_controller.update,
        methods=["PUT"],
        tags=["notifications"],
    )
    api.add_api_route(
        "/notifications",
        notification_controller.delete,
        methods=["DELETE"],
        tags=["notifications"],
    )
