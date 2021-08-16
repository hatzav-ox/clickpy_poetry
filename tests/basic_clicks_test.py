# noqa

from clickpy.click_strategy import BasicClickStrategy, SupportsClick
from pytest import CaptureFixture
from pytest_mock import MockerFixture


def test_BasicClickStrategy_is_SupportsClick():  # noqa
    assert isinstance(BasicClickStrategy(), SupportsClick)


def test_BasicClickStrategy_uses_passed_in_sleep_time(mocker: MockerFixture):  # noqa
    # Arrange
    mock_sleep = mocker.patch("clickpy.click_strategy.sleep")
    mock_gui_click = mocker.patch("clickpy.click_strategy.pyautogui.click")
    sleep_time = 3

    # Act
    basic_click = BasicClickStrategy(sleep_time=sleep_time)
    basic_click.__click__()

    # Assert
    assert basic_click.sleep_time == sleep_time
    mock_sleep.assert_called_once_with(sleep_time)
    mock_gui_click.assert_called_once()


def test_BasicClickStrategy_uses_randint_when_sleep_time_is_none(mocker: MockerFixture):  # noqa
    # Arrange
    sleep_time = 5
    mock_randint = mocker.patch("clickpy.click_strategy.randint", return_value=sleep_time)
    mock_sleep = mocker.patch("clickpy.click_strategy.sleep")
    mock_gui_click = mocker.patch("clickpy.click_strategy.pyautogui.click")

    # Act
    basic_click = BasicClickStrategy()
    basic_click.__click__()

    # Assert
    assert basic_click.sleep_time is None
    mock_randint.assert_called_once_with(basic_click.min_sleep_bound, basic_click.max_sleep_bound)
    mock_sleep.assert_called_once_with(sleep_time)
    mock_gui_click.assert_called_once()


def test_BasicClickStrategy_prints_stdout_when_print_debug_is_True(
    mocker: MockerFixture, capsys: CaptureFixture
):  # noqa
    # Arrange
    sleep_time = 1

    mock_sleep = mocker.patch("clickpy.click_strategy.sleep")
    mock_gui_click = mocker.patch("clickpy.click_strategy.pyautogui.click")

    # Act
    basic_click = BasicClickStrategy(sleep_time=sleep_time, print_debug=True)
    basic_click.__click__()

    out, err = capsys.readouterr()

    # Assert
    assert basic_click.sleep_time is sleep_time
    assert out == f"Thread sleeping now...\n... Clicked\n"
    assert err == ""
    mock_sleep.assert_called_once_with(sleep_time)
    mock_gui_click.assert_called_once()
