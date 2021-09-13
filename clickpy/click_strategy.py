"""All Clicking Strategies should be placed in this folder."""
from random import randint
from time import sleep
from typing import Optional, Protocol, runtime_checkable

import pyautogui  # type: ignore
import typer


@runtime_checkable
class SupportsClick(Protocol):
    """
    Definition of SupportsClick Protocol.

    Any object with a `__click__()` method can be considered a structural sub-type of
    SupportsClick.
    """

    debug: Optional[bool]

    def __click__(self) -> None:
        """
        Protocol method for the auto_click function.

        Any ClickStrategy class should implement a '__click__' method.
        """

    @classmethod
    def to_cli_string(cls) -> str:
        """Turn classname into a friendly, cli identifiable name.

        Returns:
            str: cli friendly class name
        """


class BasicClickStrategy:
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

    @classmethod
    def to_cli_string(cls):
        """Returns 'basic'."""
        return cls.__name__.replace("ClickStrategy", "").lower()


class NaturalClickStrategy:
    """Click Strategy to replicate a more natural clicking pattern."""

    def __init__(self, **kwargs):
        """Init fields."""
        self.debug = kwargs.get("debug")
        self._min_sleep_bound = 5
        self._max_sleep_bound = 60
        self.wait_times = [1.0, 1.0, 2.5, randint(self._min_sleep_bound, self._max_sleep_bound)]

    def __click__(self):
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

    @classmethod
    def to_cli_string(cls):
        return cls.__name__.replace("ClickStrategy", "").lower()


STRATEGIES = {
    BasicClickStrategy.to_cli_string(): BasicClickStrategy,
    NaturalClickStrategy.to_cli_string(): NaturalClickStrategy,
}
