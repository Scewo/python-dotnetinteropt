# Copyright (Python) 2024 SCEWO AG

from __future__ import annotations

from dataclasses import dataclass
import os
import shutil
import subprocess  # noqa: S404
import time
from typing import Optional

import toml

__all__ = ["install_nugets"]

_DOTNET_LIB_CSPROJ = """<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net{}</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
{}
  </ItemGroup>

</Project>
"""

_DOTNET_PACKAGE_REF = """<PackageReference Include="{}" Version="{}" />"""


@dataclass
class _DotnetConfig:
    package_name: str
    version: str
    outpath: str
    dependencies: list[list[str]]
    release: bool


def _check_dependencies() -> None:

    if shutil.which("dotnet") is None:
        raise RuntimeError("Please install dotnet first and add it to your PATH "
                           "(https://dotnet.microsoft.com/en-us/download)")


def _get_dotnet_config(dotnetconfig_toml_path: Optional[str]) -> _DotnetConfig:

    dotnetconfig_toml_path = dotnetconfig_toml_path or "pyproject.toml"

    res = subprocess.run(["dotnet", "--version"], check=True, capture_output=True)  # noqa: S603 S607
    version = res.stdout.decode("utf-8").split(".")[0].strip()
    print(f"Dotnet version: {version}")

    with open(dotnetconfig_toml_path, "r", encoding="utf-8") as pyproject_toml_file:
        pyproject = toml.load(pyproject_toml_file)

    # Default values
    package_name = None
    dependencies = []
    outpath = "_dotnetinteropt"
    release = True

    if "project" in pyproject:
        package_name = pyproject["project"].get("name") or package_name

    if "tool" in pyproject and "dotnetinteropt" in pyproject["tool"]:
        package_name = pyproject["tool"]["dotnetinteropt"].get("package") or package_name
        outpath = pyproject["tool"]["dotnetinteropt"].get("path", outpath)
        dependencies = pyproject["tool"]["dotnetinteropt"].get("dependencies", [])
        print(f"Dotnet dependencies: {dependencies}")
        release = pyproject["tool"]["dotnetinteropt"].get("release", release)

    if not package_name:
        raise RuntimeError("Please specify the package name in the pyproject.toml file. "
                           "Or use the tool.dotnetinteropt section to specify the package name.")
    else:
        package_name = package_name.replace("-", "_")

    return _DotnetConfig(package_name=package_name,
                         version=version,
                         outpath=outpath,
                         dependencies=dependencies,
                         release=release)


def _download_dotnet_dependencies(dotnet_config: _DotnetConfig) -> None:
    cproj_fname = f"{dotnet_config.package_name}.csproj"
    project_libs = []
    if "src" in os.listdir():
        outpath = os.path.join(".", "src", dotnet_config.package_name, dotnet_config.outpath)
    else:
        outpath = os.path.join(".", dotnet_config.package_name, dotnet_config.outpath)

    for package, version in dotnet_config.dependencies:
        project_libs.append(_DOTNET_PACKAGE_REF.format(package, version))

    with open(cproj_fname, "w", encoding="utf-8") as cproj_file:
        cproj_file.write(_DOTNET_LIB_CSPROJ.format(dotnet_config.version, "\n".join(project_libs)))
        cproj_file.flush()
        time.sleep(0.05)  # wait for file to be written

    try:
        compile_mode = "Release" if dotnet_config.release else "Debug"

        cmd = ["dotnet", "publish", "-c", compile_mode, "-o", outpath]

        res = subprocess.run(cmd, capture_output=True, check=False)  # noqa: S603
        print(res.stdout.decode("utf-8"))
        print(res.stderr.decode("utf-8"))
        res.check_returncode()

        # Add .gitignore
        with open(os.path.join(outpath, ".gitignore"), "w", encoding="utf-8") as gitignore_file:
            gitignore_file.write("*")
            gitignore_file.flush()
            time.sleep(0.05)  # wait for file to be written
    finally:
        os.remove(cproj_fname)


def install_nugets(dotnetconfig_toml_path: Optional[str] = None) -> None:
    """Install the dotnet dependencies specified in the pyproject.toml file.

    Args:
        dotnetconfig_toml_path (str, optional): The path to the pyproject.toml file or any other toml file
                                                containing a [tool.dotnetinteropt] section. If none is provided, the
                                                default is "pyproject.toml" in the current working directory.
    """
    _check_dependencies()
    dotnet_config = _get_dotnet_config(dotnetconfig_toml_path)
    _download_dotnet_dependencies(dotnet_config)
