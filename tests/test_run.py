import clicker

from pytest_mock import MockerFixture
import runpy


def test_run_method(mocker: MockerFixture) -> None:
    # Arrange
    mock_typer = mocker.patch("clicker.clicker.typer.run")

    # Act
    clicker.run()

    # Assert
    mock_typer.assert_called_once_with(clicker.clicker._main)


# use runpy to run python script like an actual script or module
def test___main__py(mocker: MockerFixture) -> None:
    # Arrange
    mock_typer = mocker.patch("clicker.clicker.typer.run")
    spy_run = mocker.spy(clicker, "run")

    # Act
    runpy.run_module("clicker", run_name="__main__")

    # Assert
    mock_typer.assert_called_once_with(clicker.clicker._main)
    spy_run.assert_called_once()
