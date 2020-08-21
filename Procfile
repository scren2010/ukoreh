release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn petshop.wsgi --log-file -