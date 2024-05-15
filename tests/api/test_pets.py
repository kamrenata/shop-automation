import requests
import pytest
from faker import Faker
import random
from tests.api.constants import URL


class TestPetGetEndpoints:
    fake = Faker()

    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_get_by_status(self, status):
        response = requests.get(
            f"{URL}/pet/findByStatus",
            headers={"Accept": "application/json"},
            params={"status": status},
        )
        response = response.json()
        for x in response:
            assert x["status"] == status

    def test_get_by_id(self, add_and_delete_new_pet):
        pet_id = add_and_delete_new_pet.json().get("id")
        response = requests.get(f"{URL}/pet/{pet_id}")
        data = response.json()
        # 0. the response json is not empty
        assert data
        # 1. check if the status code is 200
        assert response.status_code == 200
        # 2. check if the response data is a dict
        assert isinstance(data, dict)
        # 3. check if "name" is present
        assert "name" in data
        # 4. check if name type is str
        assert isinstance(data.get("name"), str)
        # 5. photoUrls is present
        assert "photoUrls" in data
        # 6. check photoUrls type is list
        assert isinstance(data.get("photoUrls"), list)
        # 7. petId is the same as in the curl
        assert data.get("id") == pet_id
        # 8. returned petId format is int
        assert isinstance(data.get("id"), int)
        # 9. url starts with https
        for i in data.get("photoUrls"):
            assert i.startswith("http")
        assert response.headers.get("Content-Type") == "application/json"


class TestPetPostEndpoints:
    fake = Faker()
    required_payload = {
        "name": fake.name(),
        "id": random.randint(1, 99),
        "photoUrls": ["string"],
    }

    def test_add_new_pet(self):
        response = requests.post(
            f"{URL}/pet",
            headers={"Accept": "application/json"},
            json=self.required_payload,
        )
        assert response.status_code == 200

    def test_add_pet_image(self, add_and_delete_new_pet):
        pet_id = add_and_delete_new_pet.json().get("id")
        response = requests.post(
            f"{URL}/pet/{pet_id}/uploadImage",
            headers={"Accept": "application/json"},
            json=self.required_payload,
        )
        assert response.json()

    def test_update_pet(self, add_and_delete_new_pet):
        # this test will have error 415 as there should be 'Content-Type: application/x-www-form-urlencoded'
        pet_id = add_and_delete_new_pet.json().get("id")
        pet_info = {"id": pet_id, "name": self.fake.name(), "status": "sold"}
        response = requests.post(
            f"{URL}/pet/{pet_id}",
            headers={
                "Accept": "application/json",
                "Content-Type": "multipart/form-data",
            },
            json=pet_info,
        )
        assert response.status_code == 200


class TestPetDeleteEndpoints:
    fake = Faker()

    def test_delete_pet(self, add_new_pet):
        pet_id = add_new_pet.json().get("id")
        response = requests.delete(
            f"{URL}/pet/{pet_id}", headers={"Accept": "application/json"}
        )
        assert response.status_code == 200
