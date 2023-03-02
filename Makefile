mg:
	python manage.py migrate
mk:
	python manage.py makemigrations
creat-user:
	python manage.py createsuperuser

coll:
	python manage.py collectstatic --noinput

creat-app:
	mkdir "apps/$(name)" && python manage.py startapp $(name) apps/$(name)