# Event Management System

This is a Django-based Event Management System with REST APIs for managing events, participants, and registrations. It includes features like authentication, API pagination, filtering, and handling long-running tasks using threading.

## Features

- User Authentication via email and password.
- REST APIs for managing `Events`, `Participants`, and `Registrations`.
- Long-running task handling for registration processes using threading.
- API pagination and filtering for event listings.
- Prefetching and optimization of database queries.
  
## Prerequisites

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- PostgreSQL (or any other database)

## Setup Instructions

1. **Clone the repository**:

```bash
git clone <repository_url>
cd event_management
```

## Setup virtual environment
python -m venv env
source env/bin/activate

## Install dependencies:
pip install -r requirements.txt

## Database setup
python manage.py migrate


## Setup Superuser
python manage.py createsuperuser


## run server
python manage.py runserver


## to Access API DOC
127.0.0.1/api-doc