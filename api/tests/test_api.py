import pytest
from api.models import Contact
from rest_framework.test import APIClient as Client
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestAPI:
    def test_create_contact(self):
        c = Client()

        # Test creating a new contact
        response = c.post("/api/contacts/", {
            "name": "Test Name",
            "email": "test@example.com",
            "subject": "APP",
            "message": "This is a test message.",
        })

        assert response.status_code == 201
        assert response.json() == {
            "id": 1,
            "name": "Test Name",
            "email": "test@example.com",
            "subject": "APP",
            "message": "This is a test message.",
            "status": "NEW",
        }
        assert Contact.objects.count() == 1

        # Test retrieving the created contact
        response = c.get(f"/api/contacts/{response.json()['id']}/")
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Test Name",
            "email": "test@example.com",
            "subject": "APP",
            "message": "This is a test message.",
            "status": "NEW",
        }

    def test_negative_create_contact_without_required_fields(self):
        c = Client()

        # Test creating a contact without required fields
        response = c.post("/api/contacts/", {})
        assert response.status_code == 400
        assert response.json() == {
            'email': ['This field is required.'],
            'message': ['This field is required.'],
            'name': ['This field is required.'],
            'subject': ['This field is required.']
        }
        assert Contact.objects.count() == 0

    def test_negative_create_contact_with_invalid_email(self):
        c = Client()

        # Test creating a contact with invalid email
        response = c.post("/api/contacts/", {
            "name": "Test Name",
            "email": "invalid_email",
            "subject": "APP",
            "message": "This is a test message.",
        })

        assert response.status_code == 400
        assert response.json() == {
            'email': ['Enter a valid email address.']
        }
        assert Contact.objects.count() == 0

    def test_negative_create_contact_with_status(self):
        # Create a non-admin user for this test
        non_admin_user = User.objects.create_user('nonadmin', 'nonadmin@example.com', 'password')

        c = Client()
        c.login(username=non_admin_user.username, password='password')

        # Test creating a contact with status set by user
        response = c.post("/api/contacts/", {
            "name": "Test Name",
            "email": "test@example.com",
            "subject": "APP",
            "message": "This is a test message.",
            "status": "PRG",
        })

        assert response.status_code == 400
        assert response.json() == {
            'status': ['You are not allowed to set this field.']
        }

    def test_get_contacts(self):
        c = Client()
        response = c.get("/contact/")
        assert response.status_code == 200
