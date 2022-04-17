from clickpy import NaturalClickStrategy
from clickpy.strategy import ClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture


def test_NaturalClickStrategy_is_ClickProtocol():
    """Make sure NaturalClickStrategy implements ClickProtocol."""
    assert isinstance(NaturalClickStrategy(), ClickStrategy)  # type: ignore


def test_NaturalClickStrategy_works(mocker: MockerFixture):
    """Make sure __click__() method is working as planned."""
    num = 1.0
    mock_sleep = mocker.patch("clickpy.click_strategy.natural.sleep")
    mock_randit = mocker.patch("clickpy.click_strategy.natural.randint", return_values=num)
    mock_clicker = mocker.patch("clickpy.click_strategy.natural.click")

    natural = NaturalClickStrategy()
    natural.wait_times = [num]

    natural.__click__()

    mock_sleep.assert_called_once_with(num)
    mock_clicker.assert_called_once()


def test_click_method_with_debug_flag(mocker: MockerFixture, capsys: CaptureFixture):
    """Make sure debug statements are correct."""
    num = 1.0
    mock_sleep = mocker.patch("clickpy.click_strategy.natural.sleep")
    mock_randit = mocker.patch("clickpy.click_strategy.natural.randint", return_values=num)
    mock_clicker = mocker.patch("clickpy.click_strategy.natural.click")

    natural = NaturalClickStrategy(debug=True)
    natural.wait_times = [num]

    natural.__click__()

    out, _ = capsys.readouterr()

    assert out == f"Waiting for {num} sec ...\n... Clicked\n"
    mock_sleep.assert_called_once_with(num)
    mock_clicker.assert_called_once()


def test_repr_returns_natural():
    """Make sure cli repr function returns what I think it does."""
    assert NaturalClickStrategy.cli_repr() == "natural"
