"""Unit tests for main module."""
from typing import Tuple
from unittest.mock import MagicMock

import clickpy
import typer
from clickpy.click_strategy import BasicClickStrategy
from clickpy.exception import ClickStrategyNotFound
from pytest_mock import MockerFixture
from typer.testing import CliRunner

app = typer.Typer()
app.command()(clickpy.main)

runner = CliRunner()


# Helper Functions
def _make_and_mock_basic_click(
    mocker: MockerFixture, fast=False, debug=False
) -> Tuple[BasicClickStrategy, MagicMock, MagicMock]:
    """Create a basic click object and factory mock.

    Returns:
        (BasicClickStrategy, Mock for factory, Mock for auto_click)
    """
    basic_click = BasicClickStrategy(fast=fast, debug=debug)
    return (
        basic_click,
        mocker.patch("clickpy.click_strategy_factory", return_value=basic_click),
        mocker.patch("clickpy.auto_click", side_effect=KeyboardInterrupt),
    )


# Tests


def test_main_no_options(mocker: MockerFixture) -> None:  # noqa
    # Arrange
    basic_strat, mock_factory, mock_clicker = _make_and_mock_basic_click(mocker)

    # Act
    result = runner.invoke(app)

    # Assert
    assert result.exit_code == 0
    assert (
        result.stdout
        == """Running clickpy. Enter ctrl+c to stop.

Back to work!
"""
    )
    mock_factory.assert_called_once_with(click_type=None, fast=False, debug=False)
    mock_clicker.assert_called_once_with(basic_strat)


def test_main_fast_click_option(mocker: MockerFixture) -> None:  # noqa
    # Arrange
    basic_click, mock_factory, mock_clicker = _make_and_mock_basic_click(mocker, fast=True)

    # Act
    # clickpy.main.main(fast=True, debug=False)
    result = runner.invoke(app, ["-f"])

    # Assert
    assert basic_click.sleep_time == 0.5
    assert basic_click.debug == False
    mock_factory.assert_called_once_with(click_type=None, fast=True, debug=False)
    mock_clicker.assert_called_once_with(basic_click)


def test_print_strategy_names_works_correctly():  # noqa
    result = runner.invoke(app, ["--list"])

    assert result.exit_code == 0
    assert result.stdout == "Available clicking strategies:\n\nbasic\nnatural\n"


def test_print_strategy_names_doesnot_call_factory_or_auto_click(mocker: MockerFixture):  # noqa
    _, mock_factory, mock_click = _make_and_mock_basic_click(mocker)
    result = runner.invoke(app, ["--list"])

    assert result.exit_code == 0
    mock_factory.assert_not_called()
    mock_click.assert_not_called()


def test_debug_flag_works_correctly(mocker: MockerFixture):  # noqa
    basic_click, mock_factory, mock_clicker = _make_and_mock_basic_click(mocker, debug=True)

    result = runner.invoke(app, ["-d"])

    assert result.exit_code == 0
    mock_factory.assert_called_once_with(click_type=None, fast=False, debug=True)
    mock_clicker.assert_called_once_with(basic_click)

    assert (
        result.stdout
        == """Argument list:
debug=True
fast=False
list_clicks=False
click_type=None
Using clicker type: basic

KeyboardInterrupt thrown and caught. Exiting script.
"""
    )


def test_fast_flag_gets_passed_in_correctly(mocker: MockerFixture):  # noqa
    basic_click, mock_factory, mock_click = _make_and_mock_basic_click(
        mocker, fast=True, debug=True
    )

    result = runner.invoke(app, ["--debug", "--fast"])

    assert result.exit_code == 0
    assert (
        result.stdout
        == """Argument list:
debug=True
fast=True
list_clicks=False
click_type=None
Using clicker type: basic

KeyboardInterrupt thrown and caught. Exiting script.
"""
    )

    assert basic_click.sleep_time == 0.5
    assert basic_click.debug == True
    mock_factory.assert_called_once_with(click_type=None, fast=True, debug=True)
    mock_click.assert_called_once_with(basic_click)


def test_click_type_works_for_existing_click_strategies(mocker: MockerFixture):  # noqa
    basic_click, mock_factory, mock_clicker = _make_and_mock_basic_click(mocker)

    basic = "basic"
    result = runner.invoke(app, ["--type", basic])

    assert result.exit_code == 0
    assert (
        result.stdout
        == """Running clickpy. Enter ctrl+c to stop.

Back to work!
"""
    )

    mock_factory.assert_called_once_with(click_type=basic, fast=False, debug=False)
    mock_clicker.assert_called_once_with(basic_click)


def test_click_factory_throws_ClickStrategyNotFound_and_stdout_correctly(
    mocker: MockerFixture,
):  # noqa
    mock_factory = mocker.patch("clickpy.click_strategy_factory", side_effect=ClickStrategyNotFound)
    mock_clicker = mocker.patch("clickpy.auto_click", side_effect=KeyboardInterrupt)

    bad_click_type = "something_else"
    result = runner.invoke(app, ["-t", bad_click_type])

    assert result.exit_code == 1
    assert (
        result.stdout
        == f"""Argument {bad_click_type!r} is not a valid clicker type.
Available clicking strategies:

basic
natural
"""
    )
