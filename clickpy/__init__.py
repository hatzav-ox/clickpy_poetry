"""Clickpy, Automated mouse clicking scripts."""

from typing import Optional

import typer

from clickpy.click_strats import BasicClickStrategy, ClickStrategy, NaturalClickStrategy

# from clickpy.click_strategy import STRATEGIES, auto_click, click_strategy_factory
from clickpy.exception import ClickStrategyNotFound

__all__ = ["BasicClickStrategy", "NaturalClickStrategy"]


def print_startegy_names():
    """Get simplified names of all strategies and print them to stdout."""
    typer.echo("Available click types:\n")
    for name in ClickStrategy.list_strat_names():
        typer.echo(name)


# It's okay to use function calls here, because main should only be called once
# per exceution. But the values will be parsed of typer.Option will be parsed on
# the first pass.
def main(
    debug: bool = typer.Option(False, "--debug", "-d", show_default=False),  # noqa
    fast: bool = typer.Option(False, "--fast", "-f", show_default=False),  # noqa
    list_clicks: bool = typer.Option(  # noqa
        False,
        "--list",
        "-l",
        help="Print a list of all available clicker types.",
        show_default=False,
    ),
    click_type: Optional[str] = typer.Option(None, "--type", "-t", show_default=False),  # noqa
):
    """Clickpy, Automated mouse clicking with python."""
    message = "Running clickpy. Enter ctrl+c to stop.\n"

    if debug:
        message += f"\nUsing clicker type: {click_type}\n"
        message += f"""\nArgument list:
{debug=}
{fast=}
{list_clicks=}
{click_type=}
"""

    typer.echo(message)

    try:

        if list_clicks:
            print_startegy_names()
            raise typer.Exit()

        click_strategy = ClickStrategy.new(click_name=click_type, fast=fast, debug=debug)
        if debug:
            typer.echo(f"\nClick Strategy being used: {type(click_strategy)}\n")

        while True:
            click_strategy.click()

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
