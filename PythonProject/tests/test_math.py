import pytest


def add_two_numbers(a, b):
    return a + b

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "The sum of 1 & 2 should be 3"

@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 400) == 500, "The sum of 100 & 400 should be 500"

# pytest ignored main.py and runs the test_math only
# the pytest look for file and method names that contains the word "test" or "tests"