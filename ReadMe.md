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

Run `docker-compose up`
Run `docker-compsoe run django python3 manage.py runserver 0.0.0.0:8000`

## Login in Admin UI

Go to http://localhost:8000/admin, and login with the admin credentials.

## Login in Teacher UI

Go to https://localhost:8000/, and login with a teacher credentials

## how to consume API

### Teacher

* All Teachers: `GET:`http://localhost:8000/api/teachers/`
* Teacher By ID: `GET:`http://localhost:8000/api/teachers/:id/`

### Students

* All Students: `GET:`http://localhost:8000/api/students/`
* Student by ID: `GET:`http://localhost:8000/api/student/?id=:id`
* All Student by Teacher ID: `GET:`http://localhost:8000/api/students/?id=:id&type=teacher`

## How to sort by field name

Attach field name to query string.
ex: `GET:`http://localhost:8000/api/teachers/:id/?sort=first_name`
ex: `GET:`http://localhost:8000/api/students/?sort=last_name`

## How to search by last_name

Attach search text to query string.
ex: `GET:`http://localhost:8000/api/students/?sort=last_name&search=ch`
