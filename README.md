# Event Registration System

This is an Event Registration System built with Django, Django REST Framework, Celery, Redis, Signals, Multithreading, and Logging. It allows users to create events and register for them while handling background tasks and logging.

## Features
- **CRUD Operations** for Events and Registrations
- **Django Rest Framework** APIs for event creation, listing, and registration
- **Signals** to log event creation and user registration
- **Redis & Celery** for handling asynchronous tasks (e.g., sending email notifications)
- **Multithreading** for simulating long-running tasks
- **Middleware** for logging incoming requests
- **Logging** system for tracking important actions and errors

## Project Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repository-name>.git
cd <your-repository-name>
