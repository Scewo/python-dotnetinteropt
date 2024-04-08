#!/usr/bin/env python3

from __future__ import annotations

import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("No arguments given!")
    else:
        print("Arguments given: ", ", ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
