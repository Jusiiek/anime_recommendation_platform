#!/bin/bash

# wait for db
sleep 20

# apply db migrations
echo "Apply database migrations"
python manage.py migrate user
python manage.py migrate
python manage.py createuserwithrole --username admin --email super_admin@example.com --is_superuser True --is_staff True --role SUPER_ADMIN --password 12zaqWSX!@

#start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000 --settings=config.settings
