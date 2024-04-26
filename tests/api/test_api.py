import requests
import pytest
from faker import Faker
import random
import json


class TestPetGetEndpoints:
    fake = Faker()

    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_get_by_status(self, status):
        response = requests.get(f"{self.api_url}pet/findByStatus",
                                headers={"Accept": "application/json"}, params={"status": status})
        response = response.json()
        for x in response:
            assert x["status"] == status

    @pytest.fixture
    def add_new_pet(self):
        required_payload = {
            "name": self.fake.name(),
            "id": self.fake.pyint(),
            "photoUrls": [
                self.fake.url()
                for _ in range(3)  #range now contents 3 urls
            ],
        }
        response = requests.post(f"{self.api_url}pet",
                                 headers={"Accept": "application/json"},
                                 json=required_payload)
        yield response
        requests.delete(f"{self.api_url}pet/{response.json().get('id')}")

    def test_get_by_id(self, add_new_pet):
        petId = add_new_pet.json().get("id")
        response = requests.get(f"{self.api_url}pet/{petId}",
                                headers={"Accept": "application/json"})
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
        assert data.get("id") == petId
        # 8. returned petId format is int
        assert isinstance(data.get("id"), int)
        # 9. url starts with https
        for i in data.get("photoUrls"):
            assert i.startswith("http")


class TestPetPostEndpoints:
    fake = Faker()
    required_payload = {
        "name": fake.name(),
        "id": random.randint(1, 99),
        "photoUrls": [
            "string"
        ],
    }

    def test_add_new_pet(self):
        response = requests.post(f"{self.api_url}pet",
                                 headers={"Accept": "application/json"},
                                 json=self.required_payload)
        assert response.status_code == 200

    def test_add_pet_image(self):
        response = requests.post(f"{self.api_url}pet/{petId}/uploadImage",
                                 headers={"Accept": "application/json"},
                                 json=self.required_payload)
        assert response.json()
