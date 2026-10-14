#in pytest both the file name and function name should be starting with same test_.
def test_login():
    actual_status = 200
    expected_status = 200

    assert actual_status == expected_status
#command to run in terminal: python -m pytest -v test_login.py

#Multiple cases #
def test_success_status():
    actual_status = 200
    assert actual_status == 200

def test_not_found_status():
    actual_status = 404
    assert actual_status == 404

def test_server_error_status():
    actual_status = 500
    assert actual_status == 500

####################################################################################

import requests

def test_invalid_user_api():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999",
        timeout=10
    )

    assert response.status_code == 404
    print("status_code:", response.status_code)



