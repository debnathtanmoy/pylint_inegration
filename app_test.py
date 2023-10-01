"""
test for app module

"""

from pylint_inegration import app

def test_greet_user():
    """
    TEST greet use function
    """
    assert app.greet_user("Tanmoy") == "Hello, Tanmoy!"
