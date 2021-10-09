from django.db import models

# Create your models here.
from user.models import Player
from utils.models import CreateTracker, nb


class Answer(CreateTracker):
    text = models.TextField(max_length=32)
    is_right = models.BooleanField(default=False, help_text='whether this answer is right or not')


class Question(CreateTracker):
    text = models.TextField(max_length=512)

    answers = models.ManyToManyField(Answer)


class GameRoom(CreateTracker):
    questions = models.ManyToManyField(Question)

    creator = models.ForeignKey(Player, on_delete=models.PROTECT)
    opponent = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='opponent', **nb)

    finished_at = models.DateTimeField(**nb)
    is_joinable = models.BooleanField(default=True)


class GameAnswer(CreateTracker):
    room = models.ForeignKey(GameRoom, on_delete=models.PROTECT)

    player = models.ForeignKey(Player, on_delete=models.PROTECT)

    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)

    is_right = models.BooleanField(default=False)
