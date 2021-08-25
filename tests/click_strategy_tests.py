from clickpy.click_strategy import *


def test_get_classes_returns_tuples_of_click_strategy_classes():  # noqa
    classes = get_strategies()

    assert (SupportsClick.__name__, SupportsClick) not in classes
    assert (BasicClickStrategy.__name__, BasicClickStrategy) in classes
    assert (NaturalClickStrategy.__name__, NaturalClickStrategy) in classes
