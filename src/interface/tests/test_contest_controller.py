import pytest
from pytest_mock import MockFixture

from domain.Contest.contest import Contest
from domain.Contest.database.contest_repository import ContestRepository
from domain.Contest.usecase.contest_interactor import ContestInteractor
from domain.Contest.test_helper import (
    create_contest,
    create_current_contests,
    create_recent_contests,
    create_upcoming_contests,
)

from exceptions.database import DuplicateKeyError
from exceptions.waf import DuplicateKeyHTTPException, NotFoundException

from interface.controllers.contest_controller import ContestController


@pytest.mark.asyncio
async def test_contests(mocker: MockFixture) -> None:
    mocker.patch(
        "domain.Contest.usecase.contest_interactor.ContestInteractor.upcoming_contests"
    ).return_value = create_upcoming_contests(5)
    mocker.patch(
        "domain.Contest.usecase.contest_interactor.ContestInteractor.current_contests"
    ).return_value = create_current_contests(5)
    mocker.patch(
        "domain.Contest.usecase.contest_interactor.ContestInteractor.recent_contests"
    ).return_value = create_recent_contests(5)

    controller = ContestController(None)
    want = {
        "data": {
            "upcoming": create_upcoming_contests(5),
            "current": create_current_contests(5),
            "recent": create_recent_contests(5),
        },
        "status": "Success",
    }
    assert await controller.contests() == want

@pytest.mark.asyncio
async def test_contest(mocker: MockFixture) -> None:
    mocker.patch(
        "domain.Contest.usecase.contest_interactor.ContestInteractor.contest").return_value = create_contest()

    controller = ContestController(None)
    want = {
        "data": create_contest().as_json(),
        "status": "Success",
    }
    assert await controller.contest("contest_id") == want

    # test for NotFoundException when not found contest_id
    mocker.patch("domain.Contest.usecase.contest_interactor.ContestInteractor.contest").return_value = None
    with pytest.raises(NotFoundException):
        await controller.contest("contest_id")
