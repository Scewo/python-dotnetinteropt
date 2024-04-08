import pytest

from example import greetings
from example.example import Greeter


def test_greetings_success(name_success: str):
    """Test greetings function with success.

    Args:
        name_success (str): Name of the person to greet. This is a fixture (see conftest.py).
    """
    assert greetings(name_success) == f"Hello {name_success}!"


def test_greetings_fail(name_fail: str):
    """Test greetings function with failure.

    Args:
        name_fail: Name of the person to greet. This is a fixture (see conftest.py).
    """
    with pytest.raises(ValueError, match="World is is too basic!"):
        greetings(name_fail)


def test_greeter_success(name_success: str):
    """Tests the Greeter class.

    Args:
        name_success (str): Name of the person to greet. This is a fixture (see conftest.py).
    """
    greeter = Greeter(name_success)
    assert greeter.greet() is None, "The greet method should not return anything."  # type: ignore


def test_greeter_fail(name_fail: str):
    """Tests the Greeter class."""
    greeter = Greeter(name_fail)

    with pytest.raises(ValueError, match="World is is too basic!"):
        greeter.greet()
