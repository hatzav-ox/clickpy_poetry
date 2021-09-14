"""Unit tests for Click Strategy Module."""

import inspect
from typing import Protocol

import clickpy.click_strategy as ccs
from clickpy.exception import ClickStrategyNotFound


def test_all_strats_in_STRATEGIES_dict():
    """Make sure STRATEGIES dict is always up-to-date."""
    members = inspect.getmembers(ccs, inspect.isclass)
    remove_types = [
        (ccs.ClickProtocol.__name__, ccs.ClickProtocol),
        (Protocol.__name__, Protocol),
        (ClickStrategyNotFound.__name__, ClickStrategyNotFound),
    ]

    members = list(filter(lambda x: x not in remove_types, members))

    # All classes (besides base protocol) should be in this dict
    assert len(members) == len(ccs.STRATEGIES)

    for member in members:
        cli_name = member[1].to_cli_string()
        assert cli_name in ccs.STRATEGIES
        assert ccs.STRATEGIES[cli_name] == member[1]
