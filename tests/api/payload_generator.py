from faker import Faker
from tests.api.conftest import fake


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


class UserCredentials:
    username = fake.simple_profile().get("username")
    password = fake.password

