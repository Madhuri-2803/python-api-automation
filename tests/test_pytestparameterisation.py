
import pytest

@pytest.mark.parametrize("status_code", [200, 201, 404])
def test_status_code(status_code):
    assert status_code in [200, 201, 404]

############################################################################################


##########################################################################################

import pytest
#List of tupils
@pytest.mark.parametrize("status_code, expected", [
    (200, "Success"),
    (201, "Success"),
    (404, "Failure"),
    (500, "Failure")
])
def test_status_result(status_code, expected):
    if status_code in [200 , 201]:
        actual = "Success"
    elif status_code in [404,500]:
        actual = "Failure"

    assert actual == expected

    # Then compare actual with expected using assert


################################################################################################
#Real word scenario

#import pytest
#import requests

#@pytest.mark.parametrize("user_id", [1, 2, 3])
#def test_user_api(user_id):
#    response = requests.get(
#        f"https://jsonplaceholder.typicode.com/users/{user_id}",
#       timeout=10
#   )

 #   assert response.status_code == 200

  #  user = response.json()
   # assert user["id"] == user_id


