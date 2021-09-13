import inspect
import sys
from typing import Protocol

import clickpy.click_strategy as ccs


def test_all_strats_in_STRATEGIES_dict():
    """Make sure STRATEGIES dict is always up-to-date."""
    members = inspect.getmembers(ccs, inspect.isclass)
    remove_types = [(ccs.SupportsClick.__name__, ccs.SupportsClick), (Protocol.__name__, Protocol)]

    for rm in remove_types:
        assert rm in members
        members.remove(rm)

    # All classes (besides base protocol) should be in this dict
    assert len(members) == len(ccs.STRATEGIES)

    for member in members:
        cli_name = member[1].to_cli_string()
        assert cli_name in ccs.STRATEGIES
        assert ccs.STRATEGIES[cli_name] == member[1]
