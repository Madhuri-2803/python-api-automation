import requests
import pytest
def test_invalid_login(base_url):
    response = requests.get(f"{base_url}/users/999")
    assert response.status_code == 404 , (f"expected 404 but actual status is {response.status_code}")
    data = response.json()
    assert data == {}, (f"actualBody is {data}")