import random
import pytest
from tests.api.constants import URL
from tests.api.payload_generator import UserPayload
from tests.api.__init__ import *

import requests


class TestUserPostRequests:
    fake = Faker()

    def test_create_user_with_list(self):
        response = requests.post(
            f"{URL}/user/createWithList",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=UserPayload().generate_users_payload_array(),
        )
        assert response.status_code == 200

    @pytest.mark.parametrize("user_amount", [1, 2, random.randint(3, 10)])
    def test_create_list_of_users_with_array(self, user_amount):
        response = requests.post(
            f"{URL}/user/createWithArray",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=UserPayload().generate_users_payload_multiple_array(user_amount)
        )
        assert response.status_code == 200

    def test_create_new_user_while_logged_in(self, login_user):
        response = requests.post(
            f"{URL}/user",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json=UserPayload().generate_users_payload_object(),
        )
        assert response.status_code == 200


class TestUserGetRequests:

    def test_user_login(self):
        response = requests.get(
            f"{URL}/user/login",
            params={"username": UserCredentials().username, "password": UserCredentials().password},
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

    def test_update_user_while_logged_in(self, create_user, login_user):
        username = create_user[1]
        response = requests.put(
            f"{URL}/user/{username}",
            headers={"accept": "application/json"},
            json=UserPayload().generate_users_payload_object(),
        )
        assert response.status_code == 200


class TestUserDeleteRequests:
    def test_delete_user(self, login_user, create_user):
        _, username = create_user
        response = requests.delete(
            f"{URL}/user/{username}", headers={"accept": "application/json"}
        )
        assert response.status_code == 200
