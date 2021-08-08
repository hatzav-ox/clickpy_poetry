# noqa

import clickpy
from clickpy.clickers.basic_clicks import BasicRandomClickStrategy, FastClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture


def test_main_no_options(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
    # Arrange
    mock_clickpy = mocker.patch("clickpy.cli.auto_click", side_effect=KeyboardInterrupt)
    # Act
    clickpy.cli._main(fast_click=None, debug=None)

    # Assert
    call, err = capsys.readouterr()
    mock_clickpy.assert_called_once_with(BasicRandomClickStrategy())
    assert call == "Running clickpy. Enter ctrl+c to stop.\n\nBack to work!\n"
    assert err == ""


def test_main_fast_click_option(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
    # Arrange
    mock_clickpy = mocker.patch("clickpy.cli.auto_click", side_effect=KeyboardInterrupt)

    # Act
    clickpy.cli._main(fast_click=True, debug=None)

    # Assert
    call, err = capsys.readouterr()
    mock_clickpy.assert_called_once_with(FastClickStrategy())
    assert call == "Running clickpy. Enter ctrl+c to stop.\n\nBack to work!\n"
    assert err == ""


def test_main_print_debug_option(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
    # Arrange
    mock_clickpy = mocker.patch("clickpy.cli.auto_click", side_effect=KeyboardInterrupt)

    # Act
    clickpy.cli._main(fast_click=False, debug=True)

    # Assert
    call, err = capsys.readouterr()
    mock_clickpy.assert_called_once_with(BasicRandomClickStrategy(print_debug=True))
    assert (
        call
        == "Running clickpy. Enter ctrl+c to stop.\n\nKeyboardInterrupt thrown and caught. Exiting script\n"
    )
    assert err == ""


def test_main_all_options(mocker: MockerFixture, capsys: CaptureFixture) -> None:  # noqa
    # Arrange
    mock_clickpy = mocker.patch("clickpy.cli.auto_click", side_effect=KeyboardInterrupt)

    # Act
    clickpy.cli._main(fast_click=True, debug=True)

    # Assert
    call, err = capsys.readouterr()
    mock_clickpy.assert_called_once_with(FastClickStrategy(print_debug=True))
    assert (
        call
        == "Running clickpy. Enter ctrl+c to stop.\nfast_click flag passed in. Using thread.sleep(1), instead of a random interval.\n\nKeyboardInterrupt thrown and caught. Exiting script\n"
    )
    assert err == ""
