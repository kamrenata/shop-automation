from lib.client_requests import Store


class TestStoreGetRequests:
    store = Store()

    def test_pet_inventory(self):
        response = self.store.get_pet_inventory(
            headers={"Accept": "application/json"},
            params=None
        )
        assert response.status_code == 200

    def test_find_by_order(self, place_order):
        """This test checks if the order could be found by id,
        place_order = fixture to get place an order and get order_id"""
        order_id = place_order.json().get("id")
        response = self.store.find_by_order(
            order_id,
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 200


class TestStoreDeleteRequests:
    store = Store()

    def test_delete_order_by_id(self, place_order):
        order_id = place_order.json().get("id")
        response = self.store.delete_order_by_id(
            order_id,
            headers={"Accept": "application/json"}
        )
        assert response.status_code == 200


class TestStorePostRequests:
    store = Store()

    def test_place_order_for_pet(self):
        response = self.store.place_order_for_pet()
        assert response.status_code == 200