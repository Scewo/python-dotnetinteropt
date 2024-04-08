# Copyright (Python) 2024 SCEWO AG

from __future__ import annotations

import os
import sys

from pythonnet import load as pythonnet_load

__all__ = ["load"]


def load(
        package_name: str,
        path: str = "_dotnetinteropt",
        backend: str = "coreclr",  # load the .NET Core runtime not Mono as default
) -> None:
    """Load the .NET DLLs from the specified path into the Python environment.

    Args:
        package_name (str): The name of the package to load the .NET DLLs from.
        path (str, optional): The path to the .NET DLLs. Defaults to "_dotnetinteropt".
        backend (str, optional): The backend to use. Defaults to "coreclr".
    """
    if package_name not in sys.modules:
        __import__(package_name)

    package_path = sys.modules[package_name].__path__[0]

    dotnet_dll_path = os.path.join(package_path, path)

    if dotnet_dll_path not in sys.path:
        sys.path.append(dotnet_dll_path)

    pythonnet_load(backend)
    import clr  # pylint: disable=import-outside-toplevel

    for dll in os.listdir(dotnet_dll_path):
        if dll.endswith(".dll"):
            clr.AddReference(dll.replace(".dll", ""))
