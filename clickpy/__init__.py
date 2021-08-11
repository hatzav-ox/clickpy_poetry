"""All Clicking Strategies should be placed in this folder."""

from typing import Optional

# mypy doesn't like pyautogui, and I can't find its py.types
import pyautogui  # type: ignore
import typer

from .click_strategy import BasicClickStrategy, SupportsClick

"""Auto Mouse clickpy Script. Make it look like your still online with Python Automation."""


# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False


app = typer.Typer()


def auto_click(
    click_strategy: SupportsClick,
) -> None:
    """Redo this when you've decided on a stable(ish) api."""
    # TODO: Fix docstring when a stable api is defined
    if not click_strategy:
        click_strategy = BasicClickStrategy()
    click_strategy.__click__()


@app.command()
def main(
    debug: Optional[bool] = typer.Option(None, "--debug", "-d"),
    fast_click: Optional[bool] = typer.Option(None, "--fast-click", "-f"),
) -> int:
    """Auto Mouse clickpy Script. Make it look like your still online with Python Automation."""
    print("Running clickpy. Enter ctrl+c to stop.")

    sleep_time = 1 if fast_click else None

    if debug and fast_click:
        print("fast_click flag passed in. Using thread.sleep(1), instead of a random interval.")

    click_strategy = BasicClickStrategy(sleep_time=sleep_time, print_debug=debug)
    while True:
        try:
            auto_click(click_strategy)
        except KeyboardInterrupt:
            msg = (
                "KeyboardInterrupt thrown and caught. Exiting script" if debug else "Back to work!"
            )
            print(f"\n{msg}")
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(app())  # pragma: no cover1
