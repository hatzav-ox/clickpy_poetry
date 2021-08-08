from dataclasses import dataclass
from random import randint
from time import sleep
from typing import Optional, Protocol

import pyautogui


class SupportsClick(Protocol):
    def __click__(self) -> None:
        """A dunder method for the auto_click function. Any Clicking Strategy should implement a '__click__' method."""


@dataclass
class BaseClickStrategy:
    min_sleep_time: int = 1
    max_sleep_time: int = 180
    sleep_time: Optional[int] = None
    print_debug: Optional[bool] = None

    def __click__(self) -> None:
        timer = (
            self.sleep_time
            if self.sleep_time
            else randint(self.min_sleep_time, self.max_sleep_time)
        )

        if self.print_debug:
            print(f"Random thread sleep for {timer} seconds.")

        sleep(timer)

        pyautogui.click()

        if self.print_debug:
            print("Clicked")


@dataclass
class FastClickStrategy:
    timer = 1
    print_debug: Optional[bool] = None

    def __click__(self) -> None:
        sleep(self.timer)

        if self.print_debug:
            print("Thread sleep for 1 second.")

        pyautogui.click()

        if self.print_debug:
            print("Clicked!")
