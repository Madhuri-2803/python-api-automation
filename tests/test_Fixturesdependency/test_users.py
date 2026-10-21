import pytest
import requests
def test_users(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Leanne Graham"
    assert data["id"] == 1
def test_name(base_url):
    response = requests.get(f"{base_url}/users/1")
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"
def test_name2(base_url):
    response = requests.get(f"{base_url}/users/2")
    data = response.json()
    assert data["id"] == 2
    assert data["name"] == "Ervin Howell"
def test_users_response(user_response):
   # response = requests.get(f"{base_url}/users/1")
    assert user_response.status_code == 200
    data = user_response.json()
    assert data["name"] == "Leanne Graham"
    assert data["id"] == 1

@pytest.mark.parametrize("id , name" , [ (1, "Leanne Graham") , (2, "Ervin Howell" )])
def test_multipleusers(base_url,id,name):
    response = requests.get(f"{base_url}/users/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == name


