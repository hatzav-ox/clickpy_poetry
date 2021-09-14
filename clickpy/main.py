"""Auto Mouse clickpy Script. Make it look like your still online with Python Automation."""
from typing import Optional

import pyautogui  # type: ignore # mypy doesn't like pyautogui, and I can't find its py.types
import typer

from clickpy.click_strategy import STRATEGIES, auto_click, click_strategy_factory
from clickpy.exception import ClickStrategyNotFound

# Disable FailSafeException when mouse is in screen corners.
# I don't need a failsafe for this script.
pyautogui.FAILSAFE = False


def print_startegy_names():
    """Get simplified names of all strategies and print them to cli."""
    typer.echo("Available clicking strategies:\n")
    for name in STRATEGIES.keys():
        typer.echo(name)


def main(
    click_type: Optional[str] = typer.Option(None, "--type", "-t", show_default=False),
    debug: bool = typer.Option(False, "--debug", "-d", show_default=False),
    fast: bool = typer.Option(False, "--fast", "-f", show_default=False),
    list: bool = typer.Option(
        False,
        "--list",
        "-l",
        help="Print a list of all available clicking strategies.",
        show_default=False,
    ),
):
    """Clickpy, automated mouse clicking with python."""
    try:
        if list:
            print_startegy_names()
            raise typer.Exit()

        typer.echo("Running clickpy. Enter ctrl+c to stop.")

        click_strategy = click_strategy_factory(click_type, fast=fast, debug=debug)
        if debug:
            typer.echo(f"Using clicker type: {click_strategy.to_cli_string()}")
        while True:
            auto_click(click_strategy)

    except ClickStrategyNotFound:
        typer.echo(f"{click_type} is not a valid clicker type.")
        print_startegy_names()
        raise typer.Exit(code=1)

    except KeyboardInterrupt:
        msg = "KeyboardInterrupt thrown and caught. Exiting script" if debug else "Back to work!"
        typer.echo(f"\n{msg}")


def run():
    """Run typer cli."""
    typer.run(main)


if __name__ == "__main__":
    run()  # pragma: no cover
