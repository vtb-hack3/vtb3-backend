from django.contrib import admin

# Register your models here.
from game.models import Answer, Question, GameAnswer, GameRoom


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_right')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', )


@admin.register(GameRoom)
class GameRoomAdmin(admin.ModelAdmin):
    list_display = ('creator', 'opponent')


@admin.register(GameAnswer)
class GameAnswerAdmin(admin.ModelAdmin):
    list_display = ('room', 'player', 'question', 'answer', 'is_right')
