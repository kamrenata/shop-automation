import random
import pytest
from faker import Faker
from lib.client_requests import Users
from lib.payload_generator import UserCredentials


class TestUserPostRequests:
    fake = Faker()
    users = Users()

    def test_create_user_with_list(self):
        response = self.users.create_user_with_list()
        assert response.status_code == 200

    @pytest.mark.parametrize("user_amount", [1, 2, random.randint(3, 10)])
    def test_create_list_of_users_with_array(self, user_amount):
        response = self.users.create_list_of_users_with_array(
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            user_amount=user_amount
        )
        assert response.status_code == 200


class TestUserGetRequests:
    users = Users()

    def test_user_login(self):
        response = self.users.user_login(
            headers={"Accept": "application/json"},
            params={"username": UserCredentials().username, "password": UserCredentials().password})
        assert response.status_code == 200

    def test_user_logout(self, login_user):
        response = self.users.user_logout(
            headers={"accept": "application/json"}
        )
        assert response.status_code == 200

    def test_get_user_by_username(self, create_user):
        username = create_user[1]
        response = self.users.find_user_by_username(
            username=username,
            headers={"accept": "application/json"}
        )
        assert response.status_code == 200


class TestUserPutRequests:
    users = Users()

    def test_update_user_while_logged_in(self, create_and_login_user):
        """error 500"""
        username = create_and_login_user[0]
        response = self.users.update_user_while_logged_in(
            username=username,
            headers={"accept": "application/json"}
        )
        assert response.status_code == 200


class TestUserDeleteRequests:
    users = Users()

    def test_delete_user(self, create_user):
        _, username = create_user
        response = self.users.delete_user(
            username,
            headers={"accept": "application/json"}
        )
        assert response.status_code == 200
