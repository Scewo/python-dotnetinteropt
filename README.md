# DotnetInteropt

[![build status](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/format-lint.yml/badge.svg)](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/format-lint.yml)
[![build status](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/generate-doc.yml/badge.svg)](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/generate-doc.yml)
[![build status](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/release.yml/badge.svg)](https://github.com/Scewo/python-dotnetinteropt/actions/workflows/release.yml)

This package is a tool to easily install NuGet packages and load the compiled
.NET DLL's into python. It uses [Pythonnet](https://pythonnet.github.io/) in the
background to load and run the DLL's.

In order to use this package you need to have [.NET](https://learn.microsoft.com/en-us/dotnet/core/install/)
installed and added to your PATH, verify with:

```shell
dotnet --version
```

## Usage

First, install the package:

```shell
pip install dotnetinteropt
```

Add it to the build backend dependencies:

```toml
[build-system]
requires = [..., "dotnetinteropt"]
```

And append the following to your `pyproject.toml` file:

```toml
[tool.dotnetinterop]
# OPTIONAL:

# NuGet dependencies used in the project. Can be omitted when
# no dependencies are needed:
dependencies = [
  [
    "Newtonsoft.Json",  # Replace with the actual NuGet package name
    "13.0.3", # Replace with the actual NuGet package version
  ],
  # Add more dependencies here
]
# name of the package to install it in.
# Replace with the actual package name (needed for multi-package projects)
# Otherwise the package name is inferred from the package name in the pyproject.toml:
package = "dotnetinteropt"
# path to where the DLL files should be copied to (relative to package):
path = "_dotnetinteropt" # Default
# Compiled in release or debug mode:
release = true # Default


[tool.setuptools.package-data]
"*" = ["*.dll"] # include all DLL files from all packages
```

Create a `setup.py` file in the root of your project:

```python
from setuptools import setup
from dotnetinteropt.backend import install_nugets

if __name__ == "__main__":
    install_nugets() # Has to be before setup such that it then can include the DLL's
    setup()
```

In your python code you can now load the DLL's:

```python
from dotnetinteropt import load

# Load the DLL's
load("dotnetinteropt_examples")  # Change to the package where to find the DLL's

# Now you can import the symbols from the DLL's
from Newtonsoft.Json import Formatting
from Newtonsoft.Json import JsonConvert
from System import *
from System.Collections.Generic import Dictionary
```

To generate the examples run:

```shell
make examples
```

Then run the examples with:

```shell
python3 src/dotnetinteropt_examples/hello_dotnet.py
python3 src/dotnetinteropt_examples/json_dotnet.py
```

Also, check the `pyproject.toml` file for the example configuration.

## Development

Check out the [DEVELOPMENT](DEVELOPMENT.md) file for more information on how
to develop this package.
