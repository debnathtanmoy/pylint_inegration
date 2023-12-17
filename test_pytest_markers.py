# In pytest, you can use markers to group and filter tests. Markers are a way to label 
# test functions and then use those labels to selectively run certain tests.
# To apply a marker to a test function, you can use the @pytest.mark.<marker_name> decorator, where marker_name is the name of the marker.


# pytest .\markers.py -m "slow" -> runs all tests that have the slow marker.
# pytest .\markers.py -m "number" -> runs all tests that have the number marker.
# pytest .\markers.py -m "slow or important" -> runs tests that have either the slow marker or the important marker.
# pytest .\markers.py -m "slow and not important" -> runs tests that have the slow marker and not the important marker.
# pytest .\markers.py -m "slow and important" -> runs tests that have the both the slow marker and the important marker

# pytest -k <substring of the test function> -> runs test that has the mentioned substring 
# pytest .\markers.py -k critical

import pytest

@pytest.mark.slow
@pytest.mark.important
def test_critical_function():
    assert 7+8 == 15

@pytest.mark.number
def test_add():
    assert 7+2 == 9






@pytest.mark.number
def test_subtract():
    assert 7-2 == 5