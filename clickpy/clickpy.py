"""Auto Mouse clickpy Script. Make it look like your still online with Python Automation."""

from dataclasses import dataclass
from random import randint
from time import sleep
from typing import Optional

import pyautogui

from .ClickStrategy import BaseClickStrategy, SupportsClick


def auto_click(
    click_strategy: Optional[SupportsClick],
) -> None:
    """Click function will pause current thread for a random intervaul, then click the mouse."""
    # get a time between 1 second and 3 minutes
    # to make clicks look a little more 'natural'
    if not click_strategy:
        click_strategy = BaseClickStrategy()
    click_strategy.__click__()
