from lib.client_requests import Store
from lib.constants import URL


class TestStoreGetRequests:
    store = Store()

    def test_pet_inventory(self):
        response = self.store.get_pet_inventory(
            headers={"Accept": "application/json"},
            params=None)
        assert response.status_code == 200

    # def test_find_by_order(self, place_order):
    #     order_id = place_order.get("id")
    #     response = requests.get(
    #         f"{URL}/store/order/{order_id}", headers={"Accept": "application/json"}
    #     )
    #     assert response.status_code == 200

    def test_find_by_order(self, place_order):
        order_id = place_order.get("id")
        response = requests.get(
            f"{URL}/store/order/{order_id}", headers={"Accept": "application/json"}
        )
        assert response.status_code == 200


class TestStoreDeleteRequests:
    def test_delete_order_by_id(self, place_order):
        order_id = place_order.get("id")
        response = requests.delete(
            f"{URL}/store/order/{order_id}", headers={"Accept": "application/json"}
        )
        assert response.status_code == 200


class TestStorePostRequests:
    store = Store()

    def test_place_order_for_pet(self):
        response = self.store.place_order_for_pet()
        assert response.status_code == 200

        # def test_place_order_for_pet(self, add_and_delete_new_pet, true=None):
        # required_payload = {
        #     "id": random.randint(1, 10),
        #     "petId": add_and_delete_new_pet.get("id"),
        #     "quantity": random.randint(1, 5),
        #     "shipDate": "2024-07-10T11:57:49.135Z",
        #     "status": "placed",
        #     "complete": true,
        # }
        # response = requests.post(
        #     f"{URL}/store/order",
        #     headers={"Accept": "application/json", "Content-Type": "application/json"},
        #     json=required_payload,
        # )
        #
        # assert response.status_code == 200
