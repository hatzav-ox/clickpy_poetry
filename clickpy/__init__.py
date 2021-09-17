"""Clickpy, Automated mouse clicking scripts."""

from typing import Optional

import typer

from clickpy.click_strategy import STRATEGIES, auto_click, click_strategy_factory
from clickpy.exception import ClickStrategyNotFound


def print_startegy_names():
    """Get simplified names of all strategies and print them to stdout."""
    typer.echo("Available click types:\n")
    for name in STRATEGIES.keys():
        typer.echo(name)


def main(
    debug: bool = typer.Option(False, "--debug", "-d", show_default=False),
    fast: bool = typer.Option(False, "--fast", "-f", show_default=False),
    list_clicks: bool = typer.Option(
        False,
        "--list",
        "-l",
        help="Print a list of all available clicker types.",
        show_default=False,
    ),
    click_type: Optional[str] = typer.Option(None, "--type", "-t", show_default=False),
):
    """Clickpy, Automated mouse clicking with python."""
    try:
        if debug:
            typer.echo(
                f"""Argument list:
{debug=}
{fast=}
{list_clicks=}
{click_type=}
"""
            )

        if list_clicks:
            print_startegy_names()
            raise typer.Exit()

        click_strategy = click_strategy_factory(click_type=click_type, fast=fast, debug=debug)

        message = (
            "Running clickpy. Enter ctrl+c to stop."
            if not debug
            else f"Using clicker type: {click_strategy.to_cli_string()}"
        )
        typer.echo(message)

        while True:
            auto_click(click_strategy)

    except ClickStrategyNotFound:
        typer.echo(f"Argument {click_type!r} is not a valid clicker type.")
        print_startegy_names()
        raise typer.Exit(code=1)

    except KeyboardInterrupt:
        msg = "KeyboardInterrupt thrown and caught. Exiting script." if debug else "Back to work!"
        typer.echo(f"\n{msg}")


def run():
    """Run clickpy cli with typer."""
    typer.run(main)  # pragma: no cover
