import pytest
from pytest_mock import MockFixture

from domain.Language.language import Language
from domain.Language.database.language_repository import LanguageRepository
from domain.Language.usecase.language_interactor import LanguageInteractor
from domain.Language.test_helper import create_languages

from interface.controllers.language_controller import LanguageController


@pytest.mark.asyncio
async def test_find_all(mocker: MockFixture) -> None:
    mocker.patch("domain.Language.usecase.language_interactor.LanguageInteractor.languages").return_value = create_languages(5)
    controller = LanguageController(None)
    want = {
        "data": create_languages(5),
        "status": "Success",
    }
    assert await controller.languages() == want


@pytest.mark.asyncio
async def test_create_language(mocker: MockFixture) -> None:
    mocker.patch("domain.Language.usecase.language_interactor.LanguageInteractor.store").return_value = None
    controller = LanguageController(None)
    input_data = Language(
        language="test",
        version="0.1",
        base_image="test",
        compile_command="",
        execute_command="./a.out"
    )
    want = {
        "message": "Create language",
        "status": "Success",
    }
    assert await controller.create_language(input_data) == want


@pytest.mark.asyncio
async def test_update(mocker: MockFixture) -> None:
    mocker.patch("domain.Language.usecase.language_interactor.LanguageInteractor.update").return_value = None
    controller = LanguageController(None)
    input_data = Language(
        language="test",
        version="0.1",
        base_image="test",
        compile_command="",
        execute_command="./a.out"
    )
    want = {
        "message": "Update language",
        "status": "Success",
    }
    assert await controller.update(input_data) == want


@pytest.mark.asyncio
async def test_delete(mocker: MockFixture) -> None:
    mocker.patch("domain.Language.usecase.language_interactor.LanguageInteractor.delete").return_value = None
    controller = LanguageController(None)
    language_name = "test01"
    want = {
        "status": "Success",
        "message": f"Delete language.(language={language_name})",
    }
    assert await controller.delete(language_name) == want
