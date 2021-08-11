"""Starter Clicking Strategies."""

from dataclasses import dataclass
from random import randint
from time import sleep
from typing import Callable, Optional, Protocol, runtime_checkable

import pyautogui  # type: ignore
import typer


@dataclass
class BasicClickStrategy:
    """The first random clicking strategy I came up with."""

    min_sleep_bound: int = 1
    max_sleep_bound: int = 180
    sleep_time: Optional[int] = None
    print_debug: Optional[bool] = None
    echo: Callable[[object], None] = typer.echo

    def __click__(self) -> None:
        """
        Protocol method for SupportsClick.

        Either use the sleep_time passed into the ctr, or get a random int
        between min_sleep_time and max_sleep_time.
        """
        timer = (
            self.sleep_time
            if self.sleep_time
            else randint(self.min_sleep_bound, self.max_sleep_bound)
        )

        if self.print_debug:
            self.echo(f"Random thread sleep for {timer} seconds.")

        sleep(timer)

        pyautogui.click()

        if self.print_debug:
            self.echo("Clicked")


@runtime_checkable
class SupportsClick(Protocol):  # pylint: disable=R0903
    """
       Definition of SupportsClick Protocol.

       Any object with a `click(self)` method can be considered a structural sub-type of
    SupportsClick.
    """

    def __click__(self) -> None:
        """
        Protocol method for the auto_click function.

        Any Clicking Strategy should implement a '__click__' method.
        """
