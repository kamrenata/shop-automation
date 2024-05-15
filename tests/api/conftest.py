"""Middle level conftest visible for tests directory"""
import random

import pytest
import requests
from faker import Faker
from tests.api.constants import URL
from tests.api.__init__ import *

fake = Faker()


@pytest.fixture
def add_and_delete_new_pet():
    required_payload = {
        "name": fake.name(),
        "id": fake.pyint(),
        "photoUrls": [fake.url() for _ in range(3)],  # range now contents 3 urls
    }
    response = requests.post(
        f"{URL}/pet", headers={"Accept": "application/json"}, json=required_payload
    )
    yield response
    requests.delete(f"{URL}pet/{response.json().get('id')}")


@pytest.fixture
def login_user():
    requests.get(
        f"{URL}/user/login",
        params={"username": UserCredentials().username, "password": UserCredentials().password},
        headers={"Accept": "application/json"},
    )


@pytest.fixture
def create_user(request):
    username = str(fake.simple_profile().get("username"))
    required_payload = [
        {
            "id": fake.pyint(),
            "username": username,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "phone": fake.phone_number(),
            "userStatus": 0,
        }
    ]
    response = requests.post(
        f"{URL}/user/createWithList",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        json=required_payload,
    )
    if response.status_code == 200:  # if response is 200, then request class cls returns username used to run the
        # fixture
        request.cls.username = username
        return response, username  # returns response && username
    else:
        raise AssertionError(f"Code is, {response.status_code}")


@pytest.fixture
def place_order(add_and_delete_new_pet):
    required_payload = {
        "id": random.randint(1, 10),
        "petId": add_and_delete_new_pet.json().get("id"),
        "quantity": random.randint(1, 5),
        "shipDate": "2024-07-10T11:57:49.135Z",
        "status": "placed",
        "complete": True,
    }
    return requests.post(
        f"{URL}/store/order",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        json=required_payload,
    )


@pytest.fixture
def add_new_pet(self):
    required_payload = {
        "name": self.fake.name(),
        "id": self.fake.pyint(),
        "photoUrls": [self.fake.url()],
    }
    response = requests.post(
        f"{URL}/pet", headers={"Accept": "application/json"}, json=required_payload
    )
    return response
