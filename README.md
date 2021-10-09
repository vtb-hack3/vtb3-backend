# vtb-hack-3.0
Sexy Django backend.

# How to run

## Quickstart

The fastest way to run the backend using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/ohld/django-telegram-bot
cd django-telegram-bot
```

Create virtual environment (optional)
``` bash
python3 -m venv vtb_venv
source vtb_venv/bin/activate
```

Install all requirements:
```
pip install -r requirements.txt
```

Create `.env` file in root directory and copy-paste this:
``` bash 
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Run migrations to setup SQLite database:
``` bash
python manage.py migrate
```

Create superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```

Run bot in pooling mode:
``` bash
python run_pooling.py 
```

If you want to open Django admin panel which will be located on http://localhost:8000/tgadmin/:
``` bash
python manage.py runserver
```

## Run locally using docker-compose

If you like docker-compose you can check [full instructions in our Wiki](https://github.com/ohld/django-telegram-bot/wiki/Run-locally-using-Docker-compose).

## Deploy to Production 

Read Wiki page on how to [deploy production-ready](https://github.com/ohld/django-telegram-bot/wiki/Production-Deployment-using-Dokku) scalable Telegram bot using Dokku.

----
