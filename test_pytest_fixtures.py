# In pytest, a fixture is a function that is run before each test function to set up the test environment. 
# Fixtures are a way to provide data or other dependencies that your test functions need to run.
# To define a fixture, you can use the @pytest.fixture decorator
# Pytest will pass the fixture’s return value to the test function as the argument’s value.

import pytest

@pytest.fixture
def setup_data():
    data = [1, 2, 3, 4, 5]
    return data

def test_data_length(setup_data):
    assert len(setup_data) == 5


# passing values in the fixture 
@pytest.fixture(params=[3])
def custom_list(request):
    length = request.param
    return [1] * length

def test_custom_list(custom_list):
    assert len(custom_list) == 3


@pytest.fixture(params=[1, 2])
def fixture_with_params(request):
    return request.param

def test_fixture_with_params(fixture_with_params):
    assert fixture_with_params in [1, 2, 3]