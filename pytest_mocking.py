# Mocking is a technique in which you replace certain parts of your code with mock objects during testing. 
# This can be useful when you want to test code that depends on external resources, 
# such as a database or a web service, but you don’t want to actually make the external calls during testing.

import pytest
import requests
from unittest import mock
from unittest.mock import Mock

# Mocking a function
def fetch_data_from_database():
    # fetch data from the database
    pass

def process_data():
    data = fetch_data_from_database()
    # process the data
    
# test function
@mock.patch('fetch_data_from_database')
def test_process_data(mock_fetch_data):
    mock_fetch_data.return_value = {'id': 1, 'name': 'John Doe'}
    process_data()
    # assert that the processing was done correctly

# ---------------------------------------------------------------------------------

# Mocking a library
@pytest.fixture
def mock_get(mocker):
    mock = Mock()
    mocker.patch('requests.get', return_value=mock)
    return mock

def test_get_request(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'key': 'value'}
    response = requests.get('http://example.com')
    assert response.status_code == 200
    assert response.json() == {'key': 'value'}


# ---------------------------------------------------------------------------------------

# Mocking a class instance
class Database:
    def query(self):
        # ... performing a database query
        return "Real Result"

# test_app.py
from unittest import mock
import pytest
import app

def test_database_query(mocker):
    mocked_instance = mocker.Mock(spec=app.Database)
    mocked_instance.query.return_value = "Mocked Result"
    app.Database = mocker.Mock(return_value=mocked_instance)

    db = app.Database()
    result = db.query()

    assert result == "Mocked Result"

# ---------------------------------------------------------------------------------------




# mock date time
import datetime

def get_current_date():
    return datetime.date.today()

from unittest import mock
import pytest

def test_get_current_date(mocker):
    mocked_date = datetime.date(2022, 1, 1)
    mocker.patch("datetime.date", return_value=mocked_date)
    result = app.get_current_date()
    assert result == mocked_date

# ---------------------------------------------------------------------------------------

# Mocking an s3 Bucket and if a file is present
import boto3
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_s3(mocker):
    mock = Mock(spec=boto3.client('s3'))
    mocker.patch('boto3.client', return_value=mock)
    return mock

def test_s3_upload(mock_s3):
    mock_s3.upload_file.return_value = None
    # Test code that uploads a file to S3
    # ...
    mock_s3.upload_file.assert_called_once()

def test_s3_file_exists(mock_s3):
    mock_s3.head_object.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}
    # Test code that checks if a file exists in S3
    # ...
    mock_s3.head_object.assert_called_once()