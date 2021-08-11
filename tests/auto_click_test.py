# noqa

from unittest.mock import MagicMock

import pytest
from clickpy import BasicClickStrategy, SupportsClick, auto_click


def test_auto_click_throws_type_error_if_arg_not_SupportsClick_subtype():  # noqa
    with pytest.raises(TypeError) as excinfo:
        auto_click(None)  # type: ignore

    assert excinfo.type is TypeError
    assert (
        excinfo.value.args[0] == f"Argument passed in of type {type(None)} does not implement"
        f" {SupportsClick.__name__}"
    )


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
    class SomeObj:
        name = "SomeObj"

    some_obj = SomeObj()
    mock_func = MagicMock(return_value=None, name="__click__")
    setattr(some_obj, "__click__", mock_func)

    # Act
    auto_click(some_obj)  # type: ignore

    # Assert
    some_obj.__click__.assert_called_once()  # type: ignore
