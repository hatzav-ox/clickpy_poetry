"""Definition of SupportsClick Protocol."""

from typing import Protocol


class SupportsClick(Protocol):  # pylint: disable=R0903
    """Definition of SupportsClick Protocol."""

    def click(self) -> None:
        """
        A dunder method for the auto_click function.

        Any Clicking Strategy should implement a '__click__' method.
        """
