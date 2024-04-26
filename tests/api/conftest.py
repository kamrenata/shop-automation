"""Middle level conftest visible for tests directory"""
import pytest


@pytest.fixture(autouse=True)
def set_up(request):
    request.cls.api_url = "https://petstore.swagger.io/v2/"

