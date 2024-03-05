import requests


def test_get_facts_request():
    response = requests.get("https://cat-fact.herokuapp.com/facts/", headers={"Accept": "application/json"})
    assert response.json()[0]["text"]
