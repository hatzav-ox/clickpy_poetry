# noqa

from clickpy.click_strategy import *


def test_BasicRandomClickStrategy_is_SupportsClick():  # noqa
    assert isinstance(BasicClickStrategy(), SupportsClick)
