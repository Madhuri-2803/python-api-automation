import requests
import pytest

#@pytest.fixture
#@pytest.fixture(scope="module")
@pytest.fixture(scope="class" , params=[1,2])
##using parameterization in fixtures
def user_response(request): #special pytest fixture that gives you information about the current fixture execution.
    userid = request.param ##to retrive the ID form user
    print(f"Setup: API Request Started {userid}")
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}" , timeout=10)
    assert user_response.status_code == 200 , (f"Expected statuscode=200 , but got {user_response.status_code}")
    user = user_response.json()
    assert userid == user["id"]
    yield user_response
    print(f"Teardown : API Request Completed {userid} ")

