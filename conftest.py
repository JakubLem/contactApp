import pytest
from rest_framework.test import APIClient as Client


@pytest.fixture
def client():
    def factory(uid=None, token=None):
        if not uid:
            return Client()

        client = Client()
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        return client

    return factory
