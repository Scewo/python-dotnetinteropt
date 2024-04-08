import pytest


@pytest.fixture()
def name_success() -> str:
    return "Sailer"


@pytest.fixture()
def name_fail() -> str:
    return "World"
