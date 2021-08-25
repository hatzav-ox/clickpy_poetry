"""All Clicking Strategies should be placed in this folder."""

import inspect
import sys
from dataclasses import dataclass, field
from random import randint
from time import sleep
from typing import Any, Callable, Optional, Protocol, Tuple, runtime_checkable

import pyautogui  # type: ignore
import typer


@runtime_checkable
class SupportsClick(Protocol):  # pylint: disable=R0903
    """
    Definition of SupportsClick Protocol.

    Any object with a `__click__()` method can be considered a structural sub-type of
    SupportsClick.
    """

    def __click__(self) -> None:
        """
        Protocol method for the auto_click function.

        Any ClickStrategy class should implement a '__click__' method.
        """


@dataclass
class BasicClickStrategy:
    """The first, very basic clicking strategy I came up with.

    Before clicking, __click__ will tell the current thread to sleep.
    If self.sleep_time has a value, it will use that as the thread sleep time.
    Else, it will generate a random number between 1 and 180 (3 minutes).
    """

    min_sleep_bound: int = 1
    max_sleep_bound: int = 180
    sleep_time: Optional[float] = None
    print_debug: Optional[bool] = None
    echo: Callable[[object], None] = typer.echo

    def __click__(self) -> None:
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
            else float(randint(self.min_sleep_bound, self.max_sleep_bound))
        )

        if self.print_debug and not self.sleep_time:
            self.echo(f"Random thread sleep for {timer} seconds.")

        if self.print_debug:
            self.echo("Thread sleeping now...")

        sleep(timer)

        pyautogui.click()

        if self.print_debug:
            self.echo("... Clicked")


@dataclass
class NaturalClickStrategy:
    """Click Strategy to replicate a more natural clicking pattern."""

    min_sleep_bound = 5
    max_sleep_bound = 60
    wait_times: list[float] = field(default_factory=list)

    def __post_init__(self):
        """Init list field."""
        self.wait_times = [1.0, 1.0, 2.5]

    def __click__(self):
        """Protocol method defined by SupportsClick.

        Process:
        Define a list of 'wait times', i.e. time in between clicks.
        In a loop, click mouse then sleep that iterations wait time.
        At the end, get a random time between min and max bounds.
        """
        for time in self.wait_times:
            pyautogui.click()
            sleep(time)
        else:
            time = randint(self.min_sleep_bound, self.max_sleep_bound)
            sleep(time)


def get_strategies() -> list[Tuple[str, Any]]:
    """Get all the ClickStrategy classes in this module."""
    # this should get all the classes in this module
    classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    # list of classes to remove
    remove_protocols = [(SupportsClick.__name__, SupportsClick), (Protocol.__name__, Protocol)]
    for proto in remove_protocols:
        try:
            classes.remove(proto)
        except ValueError:
            pass

    return classes


def pick_click_type(
    type: Optional[str], fast_click: Optional[float], print_debug: Optional[bool]
) -> SupportsClick:
    if not type or fast_click:
        return BasicClickStrategy(sleep_time=fast_click, print_debug=print_debug)

    strategies = get_strategies()
    for strat in strategies:
        if type.lower() in strat[0].lower():
            return strat[1]()
    else:
        return BasicClickStrategy(sleep_time=fast_click, print_debug=print_debug)
