"""All Clicking Strategies should be placed in this folder."""

import inspect
import sys
from dataclasses import dataclass, field
from random import randint
from time import sleep
from typing import Any, Optional, Protocol, Tuple, runtime_checkable

import pyautogui  # type: ignore
import typer


@runtime_checkable
class SupportsClick(Protocol):  # pylint: disable=R0903
    """
    Definition of SupportsClick Protocol.

    Any object with a `__click__()` method can be considered a structural sub-type of
    SupportsClick.
    """

    print_debug: Optional[bool]

    def __click__(self) -> None:
        """
        Protocol method for the auto_click function.

        Any ClickStrategy class should implement a '__click__' method.
        """

    @classmethod
    def get_simple_name(cls) -> str:
        """[summary]

        Returns:
            str: [description]
        """


def _get_strategies() -> list[Tuple[str, Any]]:
    """Get all the ClickStrategy classes in this module.

    Returns:
        list[Tuple[str, Any]]: [description]
    """
    # this should get all the classes in this module
    # unfortunately, this will also get the SupportsClick class
    # this will need to be removed
    members = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    # list of classes to remove
    remove_protocols = [(SupportsClick.__name__, SupportsClick), (Protocol.__name__, Protocol)]
    return [x for x in members if x not in remove_protocols]


def get_simple_names() -> list[str]:
    return [x[1].get_simple_name() for x in _get_strategies()]


def get_click_strategy(
    type: Optional[str], fast_click: Optional[float], print_debug: Optional[bool]
) -> SupportsClick:
    """Create ClickStrategy based on user input via cli.

    Args:
        type (Optional[str]): [description]
        fast_click (Optional[float]): [description]
        print_debug (Optional[bool]): [description]

    Returns:
        SupportsClick: [description]
    """
    if not type:
        return BasicClickStrategy(sleep_time=fast_click, print_debug=print_debug)

    strategies = _get_strategies()
    for strat in strategies:
        # Check if name passed in cli matches any of the classes in this module
        if type.lower() in strat[0].lower():
            strat_obj = strat[1]()
            break
    else:
        strat_obj = BasicClickStrategy(sleep_time=fast_click)

    if hasattr(strat_obj, "print_debug"):
        strat_obj.print_debug = print_debug

    # if hasattr(strat_obj, "fast_click"):
    #     strat_obj.fast_click = fast_click
    return strat_obj


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
            typer.echo(f"Random thread sleep for {timer} seconds.")

        if self.print_debug:
            typer.echo("Thread sleeping now...")

        sleep(timer)

        pyautogui.click()

        if self.print_debug:
            typer.echo("... Clicked")

    @classmethod
    def get_simple_name(cls) -> str:
        return cls.__name__.replace("ClickStrategy", "").lower()


@dataclass
class NaturalClickStrategy:
    """Click Strategy to replicate a more natural clicking pattern."""

    min_sleep_bound = 5
    max_sleep_bound = 60
    print_debug: Optional[bool] = None
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

    @classmethod
    def get_simple_name(cls) -> str:
        return cls.__name__.replace("ClickStrategy", "").lower()
