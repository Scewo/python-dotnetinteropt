# Development
## Installation

Install python 3.8:

> **NOTE**
> Always use **the lowest Python version** for which this package is compatible for!
> Like this you ensure that you do not use new features that are not compatible
> with the older versions of Python. Then **run tests for all the versions that
> you support** (see the section _Run Tests_).

On Ubuntu/Debian use:

```shell
sudo apt install python3.8
```

> **NOTE**  
> On some distributions you need to add the following [PPA repository](<https://help.ubuntu.com/stable/ubuntu-help/addremove-ppa.html.en#:~:text=Personal%20Package%20Archives%20(PPAs)%20are,from%20sources%20that%20you%20trust!>)
> in order to get access to Python <= 3.9. Use
> `sudo apt install software-properties-common && sudo add-apt-repository
 ppa:deadsnakes/ppa && sudo apt update`
> and retry the command above.

For other platforms you can check out the [Python Website](https://www.python.org/)
for download.

It is recommended to install everything into a [virtual environment](https://docs.python.org/3.9/tutorial/venv.html).
To create one:

```shell
python3 -m venv venv
```

> **NOTE**  
> On Debian/Ubuntu the additional package `python3-venv` needs to be installed
> for the above command to work:
> `sudo apt install python3-venv`

To activate it using **bash/zsh** run:

```shell
source venv/bin/activate
```

For other shells check out this table:

| Platform | Shell           | Command to activate virtual environment |
| -------- | --------------- | --------------------------------------- |
| POSIX    | bash/zsh        | `$ source venv/bin/activate`            |
|          | fish            | `$ source venv/bin/activate.fish`       |
|          | csh/tcsh        | `$ source venv/bin/activate.csh`        |
|          | PowerShell Core | `$ venv/bin/Activate.ps1`               |
| Windows  | cmd.exe         | `C:\> venv\Scripts\activate.bat`        |
|          | PowerShell      | `PS C:\> venv\Scripts\Activate.ps1`     |

## Additional Windows requirements

Install [Chocolatery](https://chocolatey.org/install#individual). Run the
following in an elevated shell (run as admin):

```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Install make using Chocolatery (elevated shell needed):

```shell
choco install make
```

## User

```shell
make setup
```

## Developer

```shell
make setup-dev
```

## Linting

To run the formatters and linters run:

```shell
make
```

Or individually,

```shell
make lint
make format
make type-check
```

Or to run only the formatting and linting on files that were added by git (`git add`):

```shell
make lint-cached
make format-cached
make type-check-cached
```

### Ignoring Linting Errors

Sometimes it can be that the linter is wrong and you need to ignore the errors
in order to commit or pass a pull request.

Try to always specify the error code that you ignore and always specify the
reason afterwards!

##### Ignoring Flake8 Errors

At the time of writing it is only possible to ignore an error for the entire
file or for one single line.

To ignore the flake8 linting for the entire file add the file in the _exclude_
section or the _per-file-ignores_ of the `.flake8` config file.

To ignore a single line use:

```python
example = lambda: 'example'  # noqa: E731 # Reason why you ignore it
```

This will only ignore the error from pycodestyle that checks for lambda
assignments and generates an `E731`. If there are other errors on the line then
those will be reported. `# noqa` is case-insensitive, without the colon the part
after `# noqa` would be ignored.

If we instead had more than one error that we wished to ignore, we could list all
of the errors with commas separating them:

```python
# noqa: E731,E123
```

Finally, if we have a particularly bad line of code, we can ignore every error
using simply `# noqa` with nothing after it.

For more information here [here](https://flake8.pycqa.org/en/latest/user/violations.html).

#### Ignoring Pylint Errors

With Pylint you have some more possibilities to ignore errors.

The pragma controls can disable/enable:

- All the violations on a single line

  ```python
  a, b = ... # pylint: disable=unbalanced-tuple-unpacking # Reason why you ignore it
  ```

- All the violations on the following line

  ```python
  # pylint: disable-next=unbalanced-tuple-unpacking # Reason why you ignore it
  ```

  ```python
  a, b = ...
  ```

- All the violations in a single scope (at the top level it ignores the error for
  the entire file)

  ```python
  def test():
      # pylint: disable=no-member
      # Reason why you ignore it
      ...
  ```

  To re-enable the errors

  ```python
      # pylint: enable=no-member
  ```

For more information read [here](https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html).

> **NOTE**  
> In order to ignore errors both in flake8 and pylint separate the pragmas with
> #, e.g. `import clr # noqa: E402 # pylint: disable=wrong-import-position # Reason why you ignore it`

##### Ignoring Mypy Errors

You can use a special comment `# type: ignore[code, ...]` to only ignore errors
with a specific error code (or codes) on a particular line, or simply ignore
all errors on a line with `#type: ignore`:

```python
s: str = "hello"
s = 1 # type: ignore  # Reason why you ignore it`
```

## Run tests

To run tests:

```shell
make test
```

To run the tests for different python versions using [tox](https://tox.wiki/en/latest/)

```shell
make tox
```

## Pin requirements

To pin all the dependencies defined in the `pyproject.toml` file into `requirements.txt` use

```shell
make pin
```

Or with all the dev-dependencies:

```shell
make pin-dev
```

Upgrading all the dependencies then can be done using:

```shell
make pin-update
# Dev dependencies:
make pin-update-dev
```

If you ever need to sync your venv with a new requirements.txt file use:

```shell
make sync
# Dev dependencies:
make sync-dev
```

## Generate documentation

To generate documentation use:

```shell
make docs
```

The generated html docs can be found in `docs/build/html` where you then can
open `index.html`.

## Update pre-commit hooks

To update all the pre-commit hooks (`.pre-commit-config.toml`) use:

```shell
make precommit-update
```

> **WARNING**  
> The additional dependencies are not updated automatically and have to be
> updated manually by bumping the version in the config file.

If you ever need to commit without running the hooks use:

```shell
git commit --no-verify
```

**Only use this in emergencies.**
