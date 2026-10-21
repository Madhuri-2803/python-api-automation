import requests
import pytest
@pytest.mark.smoke
def test_users1(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Leanne Graham"
    assert data["id"] == 1

@pytest.mark.negative
def test_invalid_login1(base_url):
    response = requests.get(f"{base_url}/users/999")
    assert response.status_code == 404 , (f"expected 404 but actual status is {response.status_code}")
    data = response.json()
    assert data == {}, (f"actualBody is {data}")

## to run this markers we need to create pytest.ini file #########################################