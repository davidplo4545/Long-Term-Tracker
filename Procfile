web: python manage.py runserver 0.0.0.0:$PORT
worker1: celery -A longterm worker --pool=solo -l info -Q scraper
worker2: celery -A longterm worker -l info -B
