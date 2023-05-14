import pytest
from api.models import Contact

@pytest.mark.django_db
class TestAPI:
    def test_create_contact(self, client):
        c = client()
        
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

    def test_negative_create_contact_without_required_fields(self, client):
        c = client()
        
        # Test creating a contact without required fields
        response = c.post("/api/contacts/", {})
        assert response.status_code == 400
        assert response.json() == {
            'email': ['This field is required.'], 
            'message': ['This field is required.'],
            'name': ['This field is required.'],
            'subject': ['This field is required.']
        }

    def test_negative_create_contact_with_invalid_email(self, client):
        c = client()

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
