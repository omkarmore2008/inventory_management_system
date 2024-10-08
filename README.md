# Google-Meet-Django

Basic google session creation and meeting link generate


## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

This guide provides the necessary steps to set up and start a Dockerized Django project.

## Prerequisites

Before you start, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Setup

### 1. Clone the Repository

First, clone the repository to your local machine:


        $ git clone https://github.com/omkarmore2008/inventory_management_system.git
        $ cd inventory_management_system

### 2. setting up environment variable
        $ cp .env.local.example .env.local


### 3. Build and Start the Containers

        $ sudo docker compose -f docker-compose.local.yml up --build

Access Swagger API documentation once the server is running, open your browser and visit:
`http://127.0.0.1:8000/api/docs`

Access documentation once the server is running, open your browser and visit:
`http://127.0.0.1:8000/api/redoc`

### 4. Bash to djago contianer and apply migrations


        $ docker exec -it inventory_management_system_local_django bash
        $ python manage.py makemigrations
        $ python manage.py migrate

### 5. Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

#### Running tests with pytest

      $ pytest

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
