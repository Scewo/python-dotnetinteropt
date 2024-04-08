# Copyright (Python) <year> SCEWO AG
"""This is an example module.

This module is used to demonstrate how to write a module docstring. It also
shows how to write a function docstring.
"""

from __future__ import annotations


def greetings(name: str) -> str:
    """Prints a greeting to the console.

    Prints a greeting to the console. The greeting is personalized for the
    provided name.

    Args:
        name: The name of the person to greet.

    Returns:
        The greeting for the name provided.

    Raises:
        ValueError: If the name is "World".
    """
    if name == "World":
        raise ValueError("World is is too basic!")
    return f"Hello {name}!"


class Greeter:
    """A class to greet people.

    This class is used to demonstrate how to write a class docstring.

    Attributes:
        name: The name of the person to greet.
    """

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> None:
        """Prints a greeting to the console.

        Prints a greeting to the console. The greeting is personalized for the
        provided name.

        Raises:
            ValueError: If the name is "World".
        """
        print(greetings(self.name))
