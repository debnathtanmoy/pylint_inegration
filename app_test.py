from pylint_inegration import app 

def test_greet_user():
    assert app.greet_user("Tanmoy") == "Hello, Tanmoy!" 