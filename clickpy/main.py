"""Auto Mouse clickpy Script. Make it look like your still online with Python Automation."""

from typing import Optional

# mypy doesn't like pyautogui, and I can't find its py.types
import pyautogui  # type: ignore
import typer

from .click_strategy import (
    SupportsClick,
    get_click_strategy,
    get_default_strategy,
    get_simplified_names,
)

# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False


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


def print_startegy_names():
    """Get simplified names of all strategies and print them to cli."""
    typer.echo("Available clicking strategies:\n")
    for name in get_simplified_names():
        typer.echo(name.replace("ClickStrategy", "").lower())


app = typer.Typer()


@app.command()
def main(
    list: Optional[bool] = typer.Option(None, "--list", "-l"),
    debug: Optional[bool] = typer.Option(None, "--debug", "-d"),
    fast_click: Optional[bool] = typer.Option(None, "--fast-click", "-f"),
    strat_type: Optional[str] = typer.Option(
        get_default_strategy().get_simplified_name(), "--type", "-t"
    ),
) -> int:
    """Clickpy, automated mouse clicking with python."""
    if list:
        print_startegy_names()
        return 0

    typer.echo("Running clickpy. Enter ctrl+c to stop.")

    sleep_time = 0.5 if fast_click else None
    if debug:
        typer.echo(f"{strat_type=}")
        if fast_click:
            typer.echo(
                f"fast_click flag passed in. default sleep time set to {sleep_time}s, "
                "instead of a random interval."
            )

    click_strategy = get_click_strategy(strat_type, fast_click=sleep_time, print_debug=debug)

    # print(click_strategy.__class__)
    while True:
        try:
            auto_click(click_strategy)
        except KeyboardInterrupt:
            msg = (
                "KeyboardInterrupt thrown and caught. Exiting script" if debug else "Back to work!"
            )
            typer.echo(f"\n{msg}")
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(app())  # pragma: no cover
