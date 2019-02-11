# Student-Teacher App

## Create Admin User

Run `docker-compose run django python3 manage.py createsuperuser`

## build

Run `docker-compose build`

## Makemigrations

Run `docker-compsoe run django python3 manage.py makemigrations`

## Migrate

Run `docker-compsoe run django python3 manage.py migrate`

## Test

Run `docker-compsoe run django python3 manage.py test`

## Run Server

Run `docker-compsoe run django python3 manage.py runserver 0.0.0.0:8000`

## Login in Admin UI

Go to http://localhost:8000/admin, and login with the admin credentials.

## Login in Teacher UI

Go to https://localhost:8000/
