import clicker

from pytest_mock import MockerFixture


def test_run_method(mocker: MockerFixture) -> None:
    # Arrange
    mock_typer = mocker.patch("clicker.clicker.typer.run")

    # Act
    clicker.run()

    # Assert
    mock_typer.assert_called_once_with(clicker.clicker._main)
