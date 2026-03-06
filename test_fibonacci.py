"""
test_fibonacci.py — keeping it a buck, we test what we ship 💯
"""

import pytest

from fibonacci import fib


class TestFibonacci:
    """Test suite for the fib() function. We ate and left no crumbs. 🍽️"""

    def test_fib_zero(self):
        assert fib(0) == 0

    def test_fib_one(self):
        assert fib(1) == 1

    def test_fib_two(self):
        assert fib(2) == 1

    def test_fib_five(self):
        assert fib(5) == 5

    def test_fib_ten(self):
        assert fib(10) == 55

    def test_fib_large(self):
        # fib(50) = 12586269025 — no cap, that's a big number bestie
        assert fib(50) == 12586269025

    def test_fib_negative_raises(self):
        """Negative input is not the vibe — should raise ValueError."""
        with pytest.raises(ValueError):
            fib(-1)

    def test_fib_negative_large_raises(self):
        with pytest.raises(ValueError):
            fib(-100)

    def test_fib_sequence_is_additive(self):
        """Classic Fibonacci property: fib(n) = fib(n-1) + fib(n-2), slay."""
        for n in range(2, 15):
            assert fib(n) == fib(n - 1) + fib(n - 2)
