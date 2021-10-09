release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker vtb.asgi:application
worker: celery -A vtb worker -P prefork --loglevel=INFO
beat: celery -A vtb beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
