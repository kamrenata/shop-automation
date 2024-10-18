from faker import Faker
import random
from _datetime import datetime


class UserPayload:
    fake = Faker()

    def generate_users_payload_array(self):
        required_payload = [
            {
                "id": self.fake.pyint(),
                "username": self.fake.simple_profile().get("username"),
                "firstName": self.fake.first_name(),
                "lastName": self.fake.last_name(),
                "email": self.fake.email(),
                "password": self.fake.password(),
                "phone": self.fake.phone_number(),
                "userStatus": 0,
            }
        ]
        return required_payload

    def generate_users_payload_object(self):
        required_payload = {
            "id": self.fake.pyint(),
            "username": self.fake.simple_profile().get("username"),
            "firstName": self.fake.first_name(),
            "lastName": self.fake.last_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
            "phone": self.fake.phone_number(),
            "userStatus": 0,
        }
        return required_payload

    def generate_users_payload_multiple_array(self, user_amount):
        required_payload = [
            {
                "id": self.fake.pyint(),
                "username": self.fake.simple_profile().get("username"),
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
        return required_payload


class UserCredentials(UserPayload):
    fake = Faker()

    username = fake.simple_profile().get("username")
    password = fake.password


class StorePayload:
    def __init__(self, pet):
        self.pet = pet

    def generate_place_pet_store_payload(self, true=None):
        current_time = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
        required_payload = {
                "id": random.randint(1, 10),
                "petId": self.pet.add_pet_and_get_id(),
                "quantity": random.randint(1, 5),
                "shipDate": current_time,
                "status": "placed",
                "complete": true
            }
        return required_payload

