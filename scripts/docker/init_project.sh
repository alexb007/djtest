#!/usr/bin/env bash

until cd /apps/djtest/
do
    echo "Waiting for django volume..."
done

python manage.py migrate &&
echo "Create superuser:" &&
python manage.py createsuperuser
