# Different types of asserts present in Pytest.

import pytest


class TestAsserts:
    def test_assert_equal(self):
        x = 10
        y = 5 + 5
        assert x == y  # Assertion passes

    def test_assert_not_equal(self):
        x = 10
        y = 5
        assert x != y  # Assertion passes

    def test_assert_true_false(self):
        x = True
        assert x  # Assertion passes

    
    def test_assert_none_values(self):
        x = None
        assert x is None # Assertion passes
    
    def test_assert_greater_less(self):
        x = 10
        y = 5
        assert x > y  # Assertion passes

    def test_assert_greater_equal_less_equal(self):
        x = 10
        y = 5
        assert x >= y  # Assertion passes

    def test_assert_in(self):
        numbers = [1, 2, 3, 4, 5]
        assert 3 in numbers  # Assertion passes

    def test_assert_not_in(self):
        numbers = [1, 2, 3, 4, 5]
        assert 6 not in numbers  # Assertion passes





