# Challenge Session 8: Parametrized Pytest for Recursive Factorial
# Problem: Write tests for a recursive factorial function using pytest parametrization.
# Hint: Use the @pytest.mark.parametrize decorator.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


import pytest
from challenge import factorial

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

