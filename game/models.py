import random
from django.db import models

# Create your models here.
from django.db.models import QuerySet

from user.models import Player
from utils.models import CreateTracker, nb


class Answer(CreateTracker):
    text = models.TextField(max_length=32)
    is_right = models.BooleanField(default=False, help_text='whether this answer is right or not')

    description = models.TextField(max_length=256)

    def __str__(self):
        return f"right: {self.is_right}, {self.text}"


class Question(CreateTracker):
    text = models.TextField(max_length=512)

    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f"{self.text}"

    @classmethod
    def get_3_random_questions(cls) -> QuerySet:
        min_id = 1
        max_id = cls.objects.first().id
        ids = [x for x in range(min_id, max_id + 1)]
        return cls.objects.filter(id__in=random.sample(ids, 3))


class GameRoom(CreateTracker):
    questions = models.ManyToManyField(Question)

    creator = models.ForeignKey(Player, on_delete=models.PROTECT)
    opponent = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='opponent', **nb)

    started_at = models.DateTimeField(**nb)
    finished_at = models.DateTimeField(**nb)
    is_joinable = models.BooleanField(default=True)


class GameAnswer(CreateTracker):
    room = models.ForeignKey(GameRoom, on_delete=models.PROTECT)

    player = models.ForeignKey(Player, on_delete=models.PROTECT)

    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)

    is_right = models.BooleanField(default=False)
