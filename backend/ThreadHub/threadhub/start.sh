#!/bin/bash
python threadhub/manage.py makemigrations authentication
python threadhub/manage.py makemigrations thread
python threadhub/manage.py migrate
python threadhub/manage.py runserver 0.0.0.0:8000