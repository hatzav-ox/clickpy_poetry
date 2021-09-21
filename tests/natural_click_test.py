from clickpy.click_strategy import ClickProtocol, NaturalClickStrategy
from pytest_mock import MockerFixture


def test_NaturalClickStrategy_is_ClickProtocol():
    assert isinstance(NaturalClickStrategy(), ClickProtocol)


def test_stuff(mocker: MockerFixture):
    num = 1
    mock_sleep = mocker.patch("clickpy.click_strategy.natural.sleep")
    mock_randit = mocker.patch("clickpy.click_strategy.natural.randint", return_values=num)

    assert False


def test_repr_returns_natural():  # noqa
    assert NaturalClickStrategy.cli_repr() == "natural"
