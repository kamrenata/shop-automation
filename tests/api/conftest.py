"""Middle level conftest visible for tests directory"""
import random
import pytest
import requests
from faker import Faker
from lib.constants import URL
from lib.client_requests import Pets
from lib.payload_generator import UserCredentials

fake = Faker()


@pytest.fixture
def add_and_delete_new_pet(add_new_pet):
    yield Pets().add_pet_and_get_id()
    Pets().delete_new_pet()


@pytest.fixture
def login_user():
    requests.get(
        f"{URL}/user/login",
        params={"username": UserCredentials().username, "password": UserCredentials().password},
        headers={"Accept": "application/json"}
    )


@pytest.fixture
def create_and_login_user():
    username = fake.simple_profile().get("username")
    password = fake.password()

    required_payload = [
        {
            "id": fake.pyint(),
            "username": username,
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "password": password,
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
        requests.get(f"{URL}/user/login",
                     params={"username": username, "password": password},
                     headers={"Accept": "application/json"}
                     )
        return username
    else:
        raise AssertionError(f"Code is, {response.status_code}")


@pytest.fixture
def create_user():
    username = fake.simple_profile().get("username")
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
        return response, username  # returns response && username
    else:
        raise AssertionError(f"Code is, {response.status_code}")


@pytest.fixture
def place_order(add_and_delete_new_pet):
    required_payload = {
        "id": random.randint(1, 10),
        "petId": add_and_delete_new_pet,
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
def add_new_pet():
    required_payload = {
        "name": fake.name(),
        "id": fake.pyint(),
        "photoUrls": [fake.url()],
    }
    response = requests.post(
        f"{URL}/pet", headers={"Accept": "application/json"}, json=required_payload
    )
    return response
