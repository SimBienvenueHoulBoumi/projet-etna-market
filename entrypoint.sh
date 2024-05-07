#!/bin/bash

set -e

conda activate etna-env

if [ "$1" = 'gunicorn' ]; then
    exec gunicorn marketplace.wsgi:application -b 0.0.0.0:8000\
        --name marketplace \
        --bind
else
    exec python manage.py runserver 0.0.0.0:8000
fi