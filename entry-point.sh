#!/bin/sh
python manage.py migrate
#python -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@alten.com', '12345678') if not User.objects.filter(username='admin') else ''"
exec "$@"