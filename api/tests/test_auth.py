import pytest
from rest_framework.test import APIClient as Client
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestUserRegistrationAndLogin:
    register_url = "/api/auth/registration/"
    login_url = "/api/auth/login/"
    test_username = "testuser"
    test_email = "test@test.com"
    test_password = "testpassword"

    def test_can_register_new_user(self):
        c = Client()

        response = c.post(self.register_url, {
            "username": self.test_username,
            "email": self.test_email,
            "password": self.test_password,
        })

        assert response.status_code == 201
        assert User.objects.count() == 1
        assert User.objects.get().username == self.test_username

    def test_can_login_existing_user(self):
        c = Client()
        c.post(self.register_url, {
            "username": self.test_username,
            "email": self.test_email,
            "password": self.test_password,
        })
        response = c.post(self.login_url, {
            "username": self.test_username,
            "password": self.test_password
        })
        assert response.status_code == 200
        assert 'token' in response.json()
