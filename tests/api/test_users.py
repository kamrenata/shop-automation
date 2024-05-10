import random

import pytest
from faker import Faker
from tests.api.conftest import fake
from tests.api.constants import URL
import requests


class TestUserPostRequests:
    fake = Faker()

    def test_create_user_with_list(self):
        required_payload = [
            {
                "id": self.fake.pyint(),
                "username": fake.simple_profile().get("username"),
                "firstName": self.fake.first_name(),
                "lastName": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.password(),
                "phone": self.fake.phone_number(),
                "userStatus": 0,
            }
        ]
        response = requests.post(
            f"{URL}/user/createWithList",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=required_payload,
        )
        assert response.status_code == 200

    @pytest.mark.parametrize("user_amount", [1, 2, random.randint(3, 10)])
    def test_create_list_of_users_with_array(self, user_amount):
        required_payload = [
            {
                "id": self.fake.pyint(),
                "username": fake.simple_profile().get("username"),
                "firstName": self.fake.first_name(),
                "lastName": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.password(),
                "phone": self.fake.phone_number(),
                "userStatus": 0,
            }
            for _ in range(user_amount)
            # b for b in list
        ]

        response = requests.post(
            f"{URL}/user/createWithArray",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=required_payload,
        )
        assert response.status_code == 200

    def test_create_new_user_while_logged_in(self, login_user):
        required_payload = {
            "id": self.fake.pyint(),
            "username": fake.simple_profile().get("username"),
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
            "phone": self.fake.phone_number(),
            "userStatus": 0,
        }
        response = requests.post(
            f"{URL}/user",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=required_payload,
        )
        assert response.status_code == 200


class TestUserGetRequests:
    fake = Faker()

    def test_user_login(self):  # works well in python console but here error 404
        response = requests.get(
            f"{URL}/user/login",
            params={"username": "john", "password": "12345"},
            headers={"Accept": "application/json"},
        )
        assert response.status_code == 200

    def test_user_logout(self, login_user):
        response = requests.get(
            f"{URL}/user/logout", headers={"accept": "application/json"}
        )
        assert response.status_code == 200

    def test_get_user_by_username(self, create_user, request):
        response = requests.get(
            f"{URL}/user/{request.cls.username}", headers={"Accept": "application/json"}
        )
        assert response.status_code == 200


class TestUserPutRequests:
    fake = Faker()

    def test_update_user_while_logged_in(self, create_user, login_user):
        required_payload = {
            "id": self.fake.pyint(),
            "username": fake.simple_profile().get("username"),
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
            "phone": self.fake.phone_number(),
            "userStatus": 0,
        }
        username = create_user.json().get("username")
        response = requests.put(
            f"{URL}/user/{username}",
            headers={"accept": "application/json"},
            json=required_payload,
        )
        assert response.status_code == 200


class TestUserDeleteRequests:
    def test_delete_user(self, login_user, create_user):
        _, username = create_user
        response = requests.delete(
            f"{URL}/user/{username}", headers={"accept": "application/json"}
        )
        assert response.status_code == 200
