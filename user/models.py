from django.db import models

from utils.models import CreateTracker


class Player(CreateTracker):
    BEGINNER = 'beginner'
    EXPERIENCED = 'experienced'
    EXPERT = 'expert'
    STATUSES = (
        (BEGINNER, 'начинающий'),
        (EXPERIENCED, 'опытный'),
        (EXPERT, 'эксперт'),
    )

    name = models.CharField(max_length=64, unique=True)

    status = models.CharField(max_length=16, choices=STATUSES, default=BEGINNER)

    picture_id = models.PositiveSmallIntegerField(default=1)

    coins = models.PositiveBigIntegerField(default=10)

