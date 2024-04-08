# Copyright (Python) <year> SCEWO AG # TODO: Change year
"""This is the main module of the example package."""

from __future__ import annotations

import argparse

from example import Greeter

_DEFAULT_NAME = "Sailer"


def _create_parser():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name",
                        type=str,
                        nargs="?",
                        default=_DEFAULT_NAME,
                        help=f"The name of the person to greet. If not provided, the name {_DEFAULT_NAME} is used.")
    return parser


def main() -> None:
    """The main function of the program.

    It takes the name of the person to greet as a command line argument. If no
    argument is provided, the name "Sailer" is used.

    Raises:
        ValueError: If the name is "World".
    """
    parser = _create_parser()
    args = parser.parse_args()
    greater = Greeter(args.name)
    greater.greet()


if __name__ == "__main__":
    main()
