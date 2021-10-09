# vtb-hack-3.0
Sexy Django backend.

## Quickstart

The fastest way to run the backend using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/vtb-hack3/vtbhack3.git
cd vtb-hack3
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


If you want to open Django admin panel which will be located on http://localhost:8000/vtbadmin/:
``` bash
python manage.py runserver
```

----
