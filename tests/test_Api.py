
import pytest
import requests

def test_user_api():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )
    print ("statusCode is :" , response.status_code)

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1

#python -m pytest -v -s test_api.py( to print results in terminal)

#########################################################################################

import requests

@pytest.mark.parametrize("user_id" ,  [1,2,3,4] )
def test_user_Api(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=10)

    assert response.status_code == 200
    user = response.json()
    assert user_id == user["id"]
    assert user["name"] != ""
###Note####
## in python use f " " to replace line 25
## look how to get store resone and how to retrive data

import requests
import pytest

@pytest.mark.parametrize("postid", [1,2,5])
def test_post_Api(postid):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{postid}" , timeout=10)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == postid
    assert user["title"] != ""
    assert user["body"] != ""

###################################################################################################
import pytest
import requests

def test_invalid_user_API():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")

    assert response.status_code == 200
    user = response.json()
    assert user == {} #Empty object 
#####we can use assert not data to check if data is empty#####

##################################################################################################
import pytest
import requests

@pytest.mark.parametrize ("userid,should_exist " ,[ 
    (1, True) , 
    (2, True) , 
    (999 , False)]
    )
def test_user_api(userid , should_exist):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    user = response.json()
    print("User ID:", userid)
    print("Status:", response.status_code, "Response:", user)
    if should_exist == True:
        assert response.status_code == 200
        assert user["id"] == userid
    else:
        assert response.status_code == 404
        assert user == {}

        

