from lib.request_wrapper import HTTPClient
from faker import Faker
from lib.payload_generator import StorePayload


class Pets(HTTPClient):
    fake = Faker()

    def __init__(self):
        super().__init__()
        # при наследовании, инициализация child & parent class

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

    def get_by_order(self, headers, params):
        route = f"store/order/{order_id}"
        order_id = place_order.get("id")
        return self.get(route, params=params, headers=headers)

    def place_order_for_pet(self):
        route = "store/order"
        required_payload = self.store_payload.generate_place_pet_store_payload()
        return self.post(route, json=required_payload)

    # def test_place_order_for_pet(self, add_and_delete_new_pet, true=None):
    #
    #         response = requests.post(
    #             f"{URL}/store/order",
    #             headers={"Accept": "application/json", "Content-Type": "application/json"},
    #             json=required_payload,
    #         )
    #
    #         assert response.status_code == 200
