"""
test for app module

"""

from ..src import app


def test_greet_user():
    """
    TEST greet use function
    """
    assert app.greet_user("Tanmoy") == "Hello, Tanmoy!"



