from django.db import models

# Create your models here.
from user.models import Player
from utils.models import CreateTracker


class Answer(CreateTracker):
    text = models.TextField(max_length=32)
    is_right = models.BooleanField(default=False, help_text='whether this answer is right or not')


class Question(CreateTracker):
    text = models.TextField(max_length=512)

    answers = models.ManyToManyField(Answer)


class Game(CreateTracker):
    questions = models.ManyToManyField(Question)


class GameAnswer(CreateTracker):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)

    player = models.ForeignKey(Player, on_delete=models.PROTECT)

    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)

    is_right = models.BooleanField(default=False)
