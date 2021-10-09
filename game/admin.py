from django.contrib import admin

# Register your models here.
from game.models import Answer, Question, Game, GameAnswer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_right')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
    # list_display = ('text', 'is_right')


@admin.register(GameAnswer)
class GameAnswerAdmin(admin.ModelAdmin):
    list_display = ('game', 'player', 'answer', 'is_right')
