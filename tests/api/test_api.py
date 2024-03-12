import requests


def test_get_facts_request():
    response = requests.get("https://cat-fact.herokuapp.com/facts/", headers={"Accept": "application/json"})
    a = response.json()
    assert response.json()[0]["text"]
    for x in a:
        assert "_id" in x
        assert isinstance(x["type"], str)
        assert isinstance(x["deleted"], bool)
        assert isinstance(x["__v"], int)


def test_get_by_status():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available",
                            headers={"Accept": "application/json"})
    response = response.json()
    for x in response:
        assert x["status"] == "available"
