"""Unit tests for main module."""
import runpy

import clickpy.main
import typer
from clickpy.click_strategy import BasicClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture
from typer.testing import CliRunner

app = typer.Typer()
app.command()(clickpy.main.main)

runner = CliRunner()


def test_main_no_options(mocker: MockerFixture) -> None:  # noqa
    # Arrange
    basic_strat = BasicClickStrategy()
    mock_factory = mocker.patch("clickpy.main.click_strategy_factory", return_value=basic_strat)
    mock_clickpy = mocker.patch("clickpy.main.auto_click", side_effect=KeyboardInterrupt)

    # Act
    result = runner.invoke(app)

    # Assert
    mock_factory.assert_called_once_with(click_type=None, fast=False, debug=False)
    mock_clickpy.assert_called_once_with(basic_strat)


# def test_main_fast_click_option(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
#     # Arrange
#     mock_clickpy = mocker.patch("clickpy.main.auto_click", side_effect=KeyboardInterrupt)

#     # Act
#     clickpy.main.main(fast_click=True, debug=None)

#     # Assert
#     call, err = capsys.readouterr()
#     mock_clickpy.assert_called_once_with(BasicClickStrategy(sleep_time=0.5))
#     assert call == "Running clickpy. Enter ctrl+c to stop.\n\nBack to work!\n"
#     assert err == ""


# def test_main_print_debug_option(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
#     # Arrange
#     mock_clickpy = mocker.patch("clickpy.main.auto_click", side_effect=KeyboardInterrupt)

#     # Act
#     clickpy.main.main(fast_click=False, debug=True)

#     # Assert
#     call, err = capsys.readouterr()
#     mock_clickpy.assert_called_once_with(BasicClickStrategy(print_debug=True))
#     assert (
#         call
#         == "Running clickpy. Enter ctrl+c to stop.\n\nKeyboardInterrupt thrown and caught. Exiting script\n"
#     )
#     assert err == ""


# def test_main_all_options(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
#     # Arrange
#     mock_clickpy = mocker.patch("clickpy.main.auto_click", side_effect=KeyboardInterrupt)

#     # Act
#     clickpy.main.main(fast_click=True, debug=True)

#     # Assert
#     call, err = capsys.readouterr()
#     mock_clickpy.assert_called_once_with(BasicClickStrategy(print_debug=True, sleep_time=0.5))
#     assert (
#         call
#         == "Running clickpy. Enter ctrl+c to stop.\nfast_click flag passed in. Using thread.sleep(1), instead of a random interval.\n\nKeyboardInterrupt thrown and caught. Exiting script\n"
#     )
#     assert err == ""


# # @pytest.mark.skip("WIP")
# def test_run_method(mocker: MockerFixture) -> None:  # noqa
#     # Arrange
#     mock_typer = mocker.patch("clickpy.app")

#     # Act
#     clickpy.app()

#     # Assert
#     mock_typer.assert_called_once_with(clickpy.main.main)


# @pytest.mark.skip("WIP")
# def test___main__py(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
#     # Arrange
#     mock_typer = mocker.patch("clickpy.main.typer.Typer")
#     spy_run = mocker.spy(clickpy.main, "main")

#     # Act
#     # use runpy to run python script like an actual script or modules
#     with pytest.raises(SystemExit) as excinfo:
#         runpy.run_module("clickpy", run_name="__main__")

#     out, err = capsys.readouterr()
#     print(out, err)
#     (retv,) = excinfo.value.args
#     # Assert
#     assert retv == 1
#     mock_typer.assert_called_once()
#     spy_run.assert_called_once()


# @pytest.mark.skip(reason="Can't figure out how to call file __main__ block.")
# def test__name_equals__main_clickpy(mocker: MockerFixture) -> None:  # noqa
#     # Arrange
#     spy_run = mocker.spy(clickpy, "run")
#     mock_typer = mocker.patch("clickpy.cli.typer.run")
#     mocker.resetall()
#     # Act
#     # runpy.run_module("clickpy", run_name="__main__")
#     runpy.run_module("clickpy.clickpy", run_name="__main__")

#     # Assert
#     mock_typer.assert_called_once_with(clickpy.cli.main)
#     spy_run.assert_called_once()
