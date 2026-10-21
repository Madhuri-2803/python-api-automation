import pytest
import requests

@pytest.fixture
def base_url():
    yield "https://jsonplaceholder.typicode.com"

@pytest.fixture
def user_response(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    yield response

    