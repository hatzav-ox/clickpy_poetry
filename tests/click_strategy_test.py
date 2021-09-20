"""Unit tests for Click Strategy Module."""

import inspect
from typing import Protocol
from unittest.mock import MagicMock

import clickpy.click_strategy
import pytest
from clickpy.click_strategy import STRATEGIES, BasicClickStrategy, ClickProtocol, auto_click
from clickpy.exception import ClickStrategyNotFound


class SomeObj:  # noqa
    def __init__(self):  # noqa
        self.x = 0


def test_all_strats_in_STRATEGIES_dict():
    """Make sure STRATEGIES dict is always up-to-date."""
    members = inspect.getmembers(clickpy.click_strategy, inspect.isclass)
    remove_types = [
        (ClickProtocol.__name__, ClickProtocol),
        (Protocol.__name__, Protocol),
        (ClickStrategyNotFound.__name__, ClickStrategyNotFound),
    ]

    members = list(filter(lambda x: x not in remove_types, members))

    # All classes (besides base protocol) should be in this dict
    assert len(members) == len(STRATEGIES)

    for member in members:
        cli_name = member[1].repr()
        assert cli_name in STRATEGIES
        assert STRATEGIES[cli_name] == member[1]


def test_auto_click_works():  # noqa
    # Arrange
    basic = BasicClickStrategy()
    basic.__click__ = MagicMock(return_value=None, name="__click__")

    # Act
    auto_click(basic)

    # Assert
    basic.__click__.assert_called_once()


def test_auto_click_structural_subtyping_works() -> None:  # noqa
    # Arrange
    some_obj = SomeObj()
    mock_click = MagicMock(return_value=None, name="__click__")
    setattr(some_obj, "__click__", mock_click)
    setattr(some_obj, "debug", False)
    setattr(some_obj, "repr", MagicMock(return_value="str", name="to_cli_string"))
    # Act
    auto_click(some_obj)  # type: ignore

    # Assert
    some_obj.__click__.assert_called_once()  # type: ignore
    mock_click.assert_called_once()
    some_obj.repr.assert_not_called()  # type: ignore


def test_auto_click_throws_type_error_if_arg_not_SupportsClick_subtype():  # noqa

    with pytest.raises(TypeError) as excinfo:
        auto_click(SomeObj())  # type: ignore

    assert excinfo.type is TypeError
    assert (
        excinfo.value.args[0] == f"Argument passed in does not implement"
        f" {ClickProtocol.__name__}"
    )
