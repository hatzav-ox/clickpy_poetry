from clickpy.click_strategy import ClickProtocol, NaturalClickStrategy
from pytest_mock import MockerFixture


def test_NaturalClickStrategy_is_instance_of_ClickProtocol():  # noqa
    assert isinstance(NaturalClickStrategy(), ClickProtocol)
