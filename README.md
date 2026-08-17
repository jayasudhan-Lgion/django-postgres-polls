# Django Polls App

A full-stack polling application built with Django and PostgreSQL. Users can view poll questions, vote on choices, and see live vote counts.

## Features

- Question and Choice models with a one-to-many relationship
- Django admin with inline choice management
- Public voting interface with real-time vote counts
- PostgreSQL database with environment-based configuration
- Template inheritance for consistent styling

## Tech stack

Python, Django, PostgreSQL, HTML/CSS

## How to run

1. Install dependencies: `pip install django psycopg2-binary python-dotenv`
2. Create a `.env` file with your database credentials (see `.env.example` structure below)
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`
6. Visit `http://127.0.0.1:8000/polls/`

## Environment variables required

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
