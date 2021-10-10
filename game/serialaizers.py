from rest_framework import serializers

from game.models import Answer, Question, GameRoom, GameAnswer
from user.models import Player
from user.serializers import PlayerSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ('created_at', )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        exclude = ('created_at', )


class GameRoomSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    creator = PlayerSerializer()
    opponent = PlayerSerializer()

    class Meta:
        model = GameRoom
        exclude = ('created_at', )


class CreateGameAnswerSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=GameRoom.objects.all())
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())

    class Meta:
        model = GameAnswer
        exclude = ('created_at', )


class ReadGameAnswerSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=GameRoom.objects.all())
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    question = QuestionSerializer()
    answer = AnswerSerializer()

    class Meta:
        model = GameAnswer
        exclude = ('created_at', 'is_right')