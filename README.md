# Django Polls App

A full-stack polling application built with Django and PostgreSQL, with user authentication and duplicate-vote prevention. Users can sign up, log in, vote on poll questions, and see live vote counts and percentages.

🔗 **Live Demo:** https://django-postgres-polls.onrender.com/polls/

## Features

- Question and Choice models with a one-to-many relationship
- Django admin with inline choice management
- User authentication: signup, login, logout
- One vote per user per question (duplicate-vote prevention)
- Voting interface with real-time vote counts and percentages
- Pagination on the poll list
- PostgreSQL database with environment-based configuration
- Template inheritance for consistent styling, with a persistent nav bar reflecting login state
- Deployed on Render with production-ready configuration (environment-based secrets, WhiteNoise static file serving, Gunicorn)

## Tech stack

Python, Django, PostgreSQL, HTML/CSS, Gunicorn, WhiteNoise — deployed on Render

## How to run locally

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with your database credentials and secret key (see structure below)
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
SECRET_KEY=your_secret_key
DEBUG=True
```
