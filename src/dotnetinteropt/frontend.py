import argparse

from .backend import install_nugets


def _main() -> int:

    parser = argparse.ArgumentParser(
        description='Install the NuGet packages specified in the config file (default is "pyproject.toml").')

    parser.add_argument("-c",
                        "--config",
                        type=str,
                        default=None,
                        help="The path to the pyproject.toml file or any other toml file "
                        "containing a [tool.dotnetinteropt] section. If none is provided, the "
                        'default is "pyproject.toml" in the current working directory.')
    args = parser.parse_args()
    install_nugets(args.config)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
