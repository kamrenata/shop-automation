from lib.request_wrapper import HTTPClient
from faker import Faker
from lib.payload_generator import StorePayload, UserPayload, UserCredentials


class Pets(HTTPClient):
    fake = Faker()

    def __init__(self):
        super().__init__()
        # init inherited class in current class in order to use its methods inside the current class

    def get_by_status(self, headers, params):
        route = "pet/findByStatus"
        return self.get(route, headers=headers, params=params)

    def get_by_id(self, headers, params):
        pet_id = self.add_pet_and_get_id()
        route = f"pet/{pet_id}"
        return self.get(route, headers=headers, params=params)

    def post_add_new_pet(self, headers, params, json):
        route = "pet"
        return self.post(route, headers=headers, params=params, json=json)

    def add_new_pet(self):
        required_payload = {
            "name": self.fake.name(),
            "id": self.fake.pyint(),
            "photoUrls": [self.fake.url() for _ in range(3)],  # range now contents 3 urls
        }
        route = "pet"
        return self.post(route, headers={"Accept": "application/json"}, json=required_payload)

    def add_pet_and_get_id(self):
        return self.add_new_pet().json().get('id')

    def delete_new_pet(self):
        pet_id = self.add_pet_and_get_id()
        route = "pet/" + str(pet_id)
        return self.delete(route)


class Store(HTTPClient):
    store_payload = StorePayload(pet=Pets())

    def __init__(self):
        super().__init__()

    def get_pet_inventory(self, headers, params):
        route = "store/inventory"
        return self.get(route, headers=headers, params=params)

    def place_order_for_pet(self):
        route = "store/order"
        required_payload = self.store_payload.generate_place_pet_store_payload()
        return self.post(route, json=required_payload)

    def find_by_order(self, order_id, headers):
        route = f"store/order/{order_id}"
        return self.get(route, headers=headers, params=None)

    def delete_order_by_id(self, order_id, headers):
        route = f"store/order/{order_id}"
        return self.delete(route, headers=headers, params=None)


class Users(HTTPClient):
    user_payload = UserPayload()
    user_credentials = UserCredentials()

    def create_user_with_list(self):
        route = "user/createWithList"
        required_payload = self.user_payload.generate_users_payload_array()
        return self.post(route, json=required_payload)

    def create_list_of_users_with_array(self, headers, user_amount):
        route = "user/createWithArray"
        required_payload = self.user_payload.generate_users_payload_multiple_array(user_amount)
        return self.post(route, json=required_payload, headers=headers)

    def user_login(self, headers, params):
        route = "user/login"
        return self.get(route, headers=headers, params=params)

    def user_logout(self, headers):
        route = "user/logout"
        return self.get(route, headers=headers, params=None)

    def find_user_by_username(self, headers, username, params=None):
        route = f"user/{username}"
        return self.get(route, headers=headers, params=params)

    def update_user_while_logged_in(self, username, headers):
        route = f"user/{username}"
        required_payload = self.user_payload.generate_users_payload_object(),
        return self.put(route, json=required_payload, headers=headers)

    def delete_user(self, username, headers):
        route = f"user/{username}"
        return self.delete(route, headers=headers)
