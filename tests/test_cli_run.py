import runpy

import clickpy
import pytest
from pytest_mock import MockerFixture


def test_run_method(mocker: MockerFixture) -> None:
    # Arrange
    mock_typer = mocker.patch("clickpy.cli.typer.run")

    # Act
    clickpy.run()

    # Assert
    mock_typer.assert_called_once_with(clickpy.cli._main)


def test___main__py(mocker: MockerFixture) -> None:
    # Arrange
    mock_typer = mocker.patch("clickpy.cli.typer.run")
    spy_run = mocker.spy(clickpy.cli, "run")

    # Act
    # use runpy to run python script like an actual script or modules
    runpy.run_module("clickpy", run_name="__main__")

    # Assert
    mock_typer.assert_called_once_with(clickpy.cli._main)
    spy_run.assert_called_once()


@pytest.mark.skip(reason="Can't figure out how to call file __main__ block.")
def test__name_equals__main_clickpy(mocker: MockerFixture) -> None:
    # Arrange
    spy_run = mocker.spy(clickpy, "run")
    mock_typer = mocker.patch("clickpy.cli.typer.run")
    mocker.resetall()
    # Act
    # runpy.run_module("clickpy", run_name="__main__")
    runpy.run_module("clickpy.clickpy", run_name="__main__")

    # Assert
    mock_typer.assert_called_once_with(clickpy.cli._main)
    spy_run.assert_called_once()
