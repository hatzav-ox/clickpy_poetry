import clicker

from pytest_mock import MockerFixture

# using pytest-mock for easier function mocking
def test_click_works(mocker: MockerFixture):
    # Arrange
    mocked_randint = mocker.patch("clicker.clicker.randint", return_value=1)
    mocked_sleep = mocker.patch("clicker.clicker.sleep")
    mocked_gui_click = mocker.patch("clicker.clicker.pyautogui.click")

    # Act
    clicker.clicker.auto_click()

    # Assert
    mocked_randint.assert_called_once()
    mocked_sleep.assert_called_once_with(1)
    mocked_gui_click.assert_called_once()


def test_fast_click_bypasses_randint(mocker: MockerFixture):
    # Arrange
    mocked_randint = mocker.patch("clicker.clicker.randint", return_value=1)
    mocked_sleep = mocker.patch("clicker.clicker.sleep")
    mocked_gui_click = mocker.patch("clicker.clicker.pyautogui.click")

    # Act
    clicker.clicker.auto_click(fast_click=True)

    # Assert
    mocked_sleep.assert_called_once_with(1)
    mocked_gui_click.assert_called_once()
    mocked_randint.assert_not_called()
