"""Middle level conftest visible for tests directory"""
import pytest
import requests
from faker import Faker
from tests.api.constants import URL

fake = Faker()


@pytest.fixture
def add_and_delete_new_pet():
    required_payload = {
        "name": fake.name(),
        "id": fake.pyint(),
        "photoUrls": [
            fake.url()
            for _ in range(3)  # range now contents 3 urls
        ],
    }
    response = requests.post(f"{URL}pet",
                             headers={"Accept": "application/json"},
                             json=required_payload)
    yield response
    requests.delete(f"{URL}pet/{response.json().get('id')}")




