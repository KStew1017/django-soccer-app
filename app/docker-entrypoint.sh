#!/bin/bash

echo "Creating database migrations"
python manage.py makemigrations

echo "Applying database migrations"
python manage.py migrate

echo "Seeding database"
python seed.py

echo "Starting server"
python manage.py runserver 0.0.0.0:8000