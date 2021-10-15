"""Click Strategy implementation using __init__subclass pattern."""
from random import randint
from time import sleep
from typing import Optional

import pyautogui
import typer

from clickpy.exception import ClickStrategyNotFound


class ClickStrategy:
    # name: str
    _strat_type = {}

    def __init_subclass__(cls, name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._strat_type[name] = cls

    def __new__(cls, name: str, **kwargs):
        try:
            subclass = cls._strat_type[name]
            obj = object.__new__(subclass)
            obj.name = name
            obj.__dict__.update(kwargs)
            # for key, value in kwargs.items():
            return obj
        except KeyError:
            raise ClickStrategyNotFound()

    def click(self):
        ...

    @classmethod
    def list_strat_names(cls):
        return list(map(lambda c: c, cls._strat_type.keys()))


class BasicClickStrategy(ClickStrategy, name="basic"):
    """The first, very basic clicking strategy I came up with.

    Before clicking, __click__ will tell the current thread to sleep.
    If self.sleep_time has a value, it will use that as the thread sleep time.
    Else, it will generate a random number between 1 and 180 (3 minutes).
    """

    def __init__(self, **kwargs):
        """Init fields."""
        self.debug = kwargs.get("debug")
        self.sleep_time = 0.5 if kwargs.get("fast") else None
        self._min_sleep_bound: int = 1
        self._max_sleep_bound: int = 180

    def click(self) -> None:
        """
        Protocol method defined by SupportsClick.

        Process:
        1. Either use the sleep_time passed into the ctr, or get a random int
        between min_sleep_time and max_sleep_time.
        2. Pause the current thread with above int (in seconds).
        3. call pyautogui.click()
        Optional: print statements if print_debug = True.
        """
        timer = (
            self.sleep_time
            if self.sleep_time
            else float(randint(self._min_sleep_bound, self._max_sleep_bound))
        )

        if self.debug and not self.sleep_time:
            typer.echo(f"Random thread sleep for {timer} seconds.")

        if self.debug:
            typer.echo("Thread sleeping now...")

        sleep(timer)
        pyautogui.click()

        if self.debug:
            typer.echo("... Clicked")


class NaturalClickStrategy(ClickStrategy, name="natural"):
    """Click Strategy to replicate a more natural clicking pattern."""

    def __init__(self, **kwargs):
        """Init fields."""
        self.debug = kwargs.get("debug")
        self._min_sleep_bound = 5
        self._max_sleep_bound = 60
        self.wait_times = [1.0, 1.0, 2.5, randint(self._min_sleep_bound, self._max_sleep_bound)]

    def click(self):
        """Protocol method defined by SupportsClick.

        Process:
        Define a list of 'wait times', i.e. time in between clicks.
        In a loop, click mouse then sleep that iterations wait time.
        At the end, get a random time between min and max bounds.
        """
        for time in self.wait_times:
            if self.debug:
                typer.echo(f"Waiting for {time} sec ...")

            sleep(time)
            pyautogui.click()

            if self.debug:
                typer.echo("... Clicked")


def auto_click(
    click_strategy: ClickStrategy,
) -> None:
    """
    Call `__click__` method of the object passed in.

    Args:
    click_strategy (SupportsClick): Should be a ClickStrategy object.

    Raises:
    TypeError: Error raised if click_strategy is not a structural subtype of SupportClicks,
    """
    if not isinstance(click_strategy, ClickStrategy):
        raise TypeError(f"Argument passed in does not implement" f" {ClickStrategy.__name__}")
    click_strategy.click()


def click_factory(
    click_type: Optional[str] = None, fast: bool = False, debug: bool = False
) -> ClickStrategy:
    """Create ClickStrategy based on cli inputs.

    Raises:
        ClickStrategyNotFound: if click_type arg does not match any known ClickStrategy.

    Returns:
        SupportsClick: ClickStrategy object that implements SupportsClick protocol.
    """
    if debug:
        typer.echo(f"click_type passed into factory func: {click_type!r}")
        if fast:
            pass
            # typer.echo(
            #     f"fast_click flag passed in. default sleep time set to {sleep_time}s, "
            #     "instead of a random interval."
            # )

    # this is the base case, nothing passed in for click_type.
    # empty string should throw exception
    if click_type is None:
        return ClickStrategy(name="basic", debug=debug, fast=fast)

    cleaned_type = click_type.strip().lower()
    if debug:
        typer.echo(f"sanitized click_type={cleaned_type!r}")

    try:
        return ClickStrategy(name=cleaned_type, debug=debug, fast=fast)
    except ClickStrategyNotFound:
        raise
