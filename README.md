# Contact Form App

This is a Django application that implements a contact form. Users can submit messages through the HTML form or REST API.

## Application Features

1. Contact Form with the following fields:
   - Name (required, 5-50 characters)
   - Email (required, valid email format including non-standard TLDs e.g: .agency, .movie, etc.)
   - Subject (required, select with 4 possible options: App Support, Payment Support, HR/Jobs, Other)
   - Message (required, up to 500 characters)
   - Status (not visible on the HTML form, possible options: New, In Progress, Resolved)

2. User-accessible page with a HTML form at the path: /contact
3. Form validation upon submission with clear error messages for invalid fields
4. Preservation of user’s input in form fields in case of submission errors
5. Confirmation message on successful form submission
6. User login page
7. Admin view for all user-submitted entries
8. Admin capabilities to change the status of a contact message
9. REST endpoint for submitting Contact form entries

## Technical Requirements

- Django framework, min version: 4.1.5
- Application developed using Django API
- Unit tests for all custom components/modules
- Docker compose file to run the application in a Docker environment

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system
- Python 3

### Building the Docker image

```bash
docker-compose build
```

### Running the Application

To start the application, run the following command:

```bash
docker-compose up
```

The application will be available at `http://localhost:8000`

### Running Tests

To run the unit tests, use the following command:

```bash
docker-compose run web pytest
```

### Running Pylama

To run Pylama for code linting, use the following command:

```bash
docker-compose run web pylama .
```

### Database Migration

To perform a database migration, run the following command:

```bash
docker-compose run web python manage.py migrate
```

### Creating a Superuser

To create a superuser for the Django Admin interface, run the following command and follow the prompts:

```bash
docker-compose run web python manage.py createsuperuser
```

## Acknowledgments

- Django
- Docker
- Pylama
- pytest
- PostgreSQL
