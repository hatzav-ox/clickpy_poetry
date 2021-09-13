"""Auto Clicker Module."""


from typing import Optional

import typer

from clickpy.click_strategy import STRATEGIES, BasicClickStrategy, SupportsClick


def auto_click(
    click_strategy: SupportsClick,
) -> None:
    """
    Call `__click__` method of the object passed in.

    Args:
    click_strategy (SupportsClick): Should be a ClickStrategy object.

    Raises:
    TypeError: Error raised if click_strategy is not a structural subtype of SupportClicks,
    """
    if not isinstance(click_strategy, SupportsClick):
        raise TypeError(
            f"Argument passed in of type {type(click_strategy)} does not implement"
            f" {SupportsClick.__name__}"
        )
    click_strategy.__click__()


# Sentinel value for factory
NO_CLICK_TYPE = ()


def click_strategy_factory(
    click_type: Optional[str] = None, fast: bool = False, debug: bool = False
) -> SupportsClick:
    """Create ClickStrategy based on cli inputs.

    Raises:
        ClickStrategyNotFound: if click_type arg does not match any known ClickStrategy.

    Returns:
        SupportsClick: ClickStrategy object that implements SupportsClick protocol.
    """
    if debug:
        typer.echo(f"{click_type=}")
        if fast:
            pass
            # typer.echo(
            #     f"fast_click flag passed in. default sleep time set to {sleep_time}s, "
            #     "instead of a random interval."
            # )
    # using this syntax, instead of not click_type, beacuse users can enter an empty string
    # empty strings should throw an Exception
    if click_type is None:
        return BasicClickStrategy(debug=debug, fast=fast)

    try:
        return STRATEGIES[click_type](debug=debug, fast=fast)
    except KeyError:
        raise ClickStrategyNotFound()


class ClickStrategyNotFound(Exception):
    """Click Type does not match any known ClickStrategy."""
