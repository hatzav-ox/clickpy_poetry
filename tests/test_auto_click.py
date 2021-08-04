import clickpy
from pytest import CaptureFixture
from pytest_mock import MockerFixture


# using pytest-mock for easier function mocking
def test_click_works(mocker: MockerFixture) -> None:
    # Arrange
    mocked_randint = mocker.patch("clickpy.clickpy.randint", return_value=5)
    mocked_sleep = mocker.patch("clickpy.clickpy.sleep")
    mocked_gui_click = mocker.patch("clickpy.clickpy.pyautogui.click")

    # Act
    clickpy.auto_click()

    # Assert
    mocked_randint.assert_called_once()
    mocked_sleep.assert_called_once_with(mocked_randint.return_value)
    mocked_gui_click.assert_called_once()


def test_auto_click_uses_sleep_time(mocker: MockerFixture) -> None:
    # Arrange
    mocked_randint = mocker.patch("clickpy.clickpy.randint", return_value=120)
    mocked_sleep = mocker.patch("clickpy.clickpy.sleep")
    mocked_gui_click = mocker.patch("clickpy.clickpy.pyautogui.click")

    timer = 3

    # Act
    clickpy.auto_click(sleep_time=timer)

    # Assert
    mocked_randint.assert_not_called()
    mocked_sleep.assert_called_once_with(timer)
    mocked_gui_click.assert_called_once()


def test_print_debug_in_auto_click(
    mocker: MockerFixture, capsys: CaptureFixture
) -> None:
    # Arrange
    mocked_randint = mocker.patch("clickpy.clickpy.randint", return_value=3)
    mocked_sleep = mocker.patch("clickpy.clickpy.sleep")
    mocked_gui_click = mocker.patch("clickpy.clickpy.pyautogui.click")

    # Act
    clickpy.auto_click(print_debug=True)

    # Assert
    out, err = capsys.readouterr()
    assert (
        out
        == f"Random thread sleep for {mocked_randint.return_value} seconds.\nClicked\n"
    )
    assert err == ""
    mocked_randint.assert_called_once()
    mocked_sleep.assert_called_once_with(mocked_randint.return_value)
    mocked_gui_click.assert_called_once()


def test_auto_click_print_debug_uses_sleep_time(
    mocker: MockerFixture, capsys: CaptureFixture
) -> None:
    # Arranged
    mock_sleep = mocker.patch("clickpy.clickpy.sleep")
    mocked_randint = mocker.patch("clickpy.clickpy.randint", return_value=42)
    mocked_gui_click = mocker.patch("clickpy.clickpy.pyautogui.click")
    timer = 2
    # Act
    clickpy.auto_click(sleep_time=timer, print_debug=True)

    # Assert
    out, err = capsys.readouterr()
    assert out == f"Random thread sleep for {timer} seconds.\nClicked\n"
    assert err == ""
    mocked_randint.assert_not_called()
    mock_sleep.assert_called_once_with(timer)
    mocked_gui_click.assert_called_once()
