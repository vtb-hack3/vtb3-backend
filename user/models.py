from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import CreateTracker


class Player(CreateTracker, AbstractUser):
    BEGINNER = 'beginner'
    EXPERIENCED = 'experienced'
    EXPERT = 'expert'
    PROFI = 'profi'
    STATUSES = (
        (BEGINNER, 'начинающий'),
        (EXPERIENCED, 'опытный'),
        (EXPERT, 'эксперт'),
        (PROFI, 'профи'),
    )

    status = models.CharField(max_length=16, choices=STATUSES)

    logo_url = models.URLField(max_length=1024)
