"""Auto Mouse Clicker Script. Make it look like your still online with Python Automation."""

from typing import Optional
from time import sleep
from random import randint

import pyautogui
import typer


# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False

# Flag to print debug statements to console.
_PRINT_DEBUG = False


def auto_click(fast_click: Optional[bool]) -> None:
    """Click function will pause current thread for a random intervaul, then click the mouse."""
    # get a time between 1 second and 3 minutes
    # to make clicks look a little more 'natural'
    global _PRINT_DEBUG

    sleep_time = 1 if fast_click else randint(1, 180)

    if _PRINT_DEBUG:
        print(
            f"Random thread sleep for {sleep_time} {'seconds' if sleep_time > 1 else 'second'}."
        )

    # pause the current thread
    sleep(sleep_time)

    # it's that easy to click a mouse with python :)
    pyautogui.click()

    if _PRINT_DEBUG:
        print("Clicked")


def main(
    debug: bool = typer.Option(None, "--debug", "-d"),
    fast_click: bool = typer.Option(None, "--fast-click", "-f"),
) -> None:
    """Auto Mouse Clicker Script. Make it look like your still online with Python Automation." """
    print("Running clicker. Enter ctrl+c to stop.")

    global _PRINT_DEBUG
    _PRINT_DEBUG = debug

    if _PRINT_DEBUG and fast_click:
        print(
            "fast_click flag passed in. Using thread.sleep(1), instead of a random interval."
        )

    while True:
        try:
            auto_click(fast_click)
        except KeyboardInterrupt:
            msg = (
                "KeyboardInterrupt thrown and caught. Exiting script"
                if _PRINT_DEBUG
                else "Back to work!"
            )
            print(f"\n{msg}")
            break

def run() -> None:
    """Common entry point."""
    typer.run(main)

if __name__ == "__main__":
    run()
