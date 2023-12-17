# Different types of asserts present in Pytest.

import pytest


class TestAsserts:
    def test_assert_equal(self):
        x = 10
        y = 5 + 5
        assert x == y  # Assertion passes
        assert x == y + 1  # Assertion fails

    def test_assert_not_equal(self):
        x = 10
        y = 5
        assert x != y  # Assertion passes
        assert x != x  # Assertion fails

    def test_assert_true_false(self):
        x = True
        assert x  # Assertion passes
        assert not x # Assertion fails

    
    def test_assert_none_values(self):
        x = None
        assert x is None # Assertion passes
        assert x is not None # Assertion fails
    
    def test_assert_greater_less(self):
        x = 10
        y = 5
        assert x > y  # Assertion passes
        assert x < y  # Assertion fails

    def test_assert_greater_equal_less_equal(self):
        x = 10
        y = 5
        assert x >= y  # Assertion passes
        assert x <= y  # Assertion fails

    def test_assert_in(self):
        numbers = [1, 2, 3, 4, 5]
        assert 3 in numbers  # Assertion passes
        assert 6 in numbers  # Assertion fails

    def test_assert_not_in(self):
        numbers = [1, 2, 3, 4, 5]
        assert 6 not in numbers  # Assertion passes
        assert 3 not in numbers  # Assertion fails





