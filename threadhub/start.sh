#!/bin/bash
python manage.py makemigrations authentication
python manage.py makemigrations thread
python manage.py migrate
python manage.py runserver