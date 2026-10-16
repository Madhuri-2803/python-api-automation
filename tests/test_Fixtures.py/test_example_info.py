#A fixture lets you prepare reusable data or setup for multiple tests, 
# instead of repeating the same code in every test.
#yield in fixture is used to clear the data after running it
#conftest is useed to use the returned data in any test file

import pytest
import requests


@pytest.fixture
def user_response():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )
    return response


def test_user_status_code(user_response):
    assert user_response.status_code == 200


def test_user_name(user_response):
    data = user_response.json()
    assert data["name"] == "Leanne Graham"


####Using Yield ####################################################################
import pytest


@pytest.fixture
##@pytest.fixture(scope="module")## helps 
def sample_user():
    print("\nSetup: Preparing user data")

    user = {"name": "Madhuri", "role": "QA Engineer"}

    yield user

    print("\nTeardown: Cleaning up after test")


def test_user_name(sample_user):
    assert sample_user["name"] == "Madhuri"


def test_user_role(sample_user):
    assert sample_user["role"] == "QA Engineer"
    
###############################################confest is useed to use the returned data in any test file################################
###Note#############
#@pytest.fixture defines reusable setup.
#conftest.py makes fixtures available to relevant test files without importing them manually.
#yield provides the response to the test and allows teardown code to run afterward.
#user_response.json() extracts the API response body as Python data.
#.status_code accesses the HTTP status code.
##@pytest.fixture(scope="module")## helps to run the API requests only onece no mater how many test are using the fixture
##@pytest.fixture## every time when test is run the API request starts