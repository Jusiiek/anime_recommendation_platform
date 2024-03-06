dev_install:
	@pip install -r ./requirements.txt

dev_run:
	@python manage.py runserver 0.0.0.0:8000 --settings=config.settings

dev_apply_migrates:
	echo "Apply database migrations"
	@python manage.py migrate user
	@python manage.py migrate
	@python manage.py createsuperuser --username admin --email admin@example.com --is_superuser True --is_staff True --role SUPER_ADMIN --password admin
