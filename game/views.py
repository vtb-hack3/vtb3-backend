from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from game.models import GameRoom, Question, GameAnswer
from game.serialaizers import GameRoomSerializer, ReadGameAnswerSerializer, AnswerSerializer
from user.models import Player
from utils.api import CustomJsonResponse


class SearchGameAPIView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        player = Player.objects.get(id=user_id)
        joinable_games = GameRoom.objects.filter(is_joinable=True)
        if joinable_games.exists():  # someone already searching for a game
            game_room = joinable_games.first()
            if game_room.creator == player:
                event_type = 'my_exist'
            else:
                game_room.opponent = player
                game_room.is_joinable = False
                game_room.started_at = datetime.now()
                game_room.save()

                event_type = 'found_room'
        else:
            game_room = GameRoom.objects.create(creator=player)
            random_questions = Question.get_3_random_questions()

            game_room.questions.add(*random_questions)

            event_type = 'created_new'

        data = {
            'type': event_type,
            'room': GameRoomSerializer(game_room).data
        }
        return CustomJsonResponse(data=data)


class CreateGameRoomAnswerAPIView(APIView):
    def post(self, request, room_id, *args, **kwargs):
        data = request.data

        user_id = data['user_id']
        question_id = data['question_id']
        answer_id = data['answer_id']

        if not GameAnswer.objects.filter(room_id=room_id, player_id=user_id, question_id=question_id).exists():
            game_answer = GameAnswer.objects.create(
                room_id=room_id,
                player_id=user_id,
                question_id=question_id,
                answer_id=answer_id,
            )
            data = ReadGameAnswerSerializer(game_answer).data
            error = None
        else:
            data = None
            error = f"Answer already exists."

        return CustomJsonResponse(data=data, errors=error)


class CountTotalAnswersAPIView(APIView):
    def post(self, request, room_id, *args, **kwargs):
        data = request.data

        user_id = data['user_id']

        total_answers = GameAnswer.objects.filter(room_id=room_id, player_id=user_id).count()

        return CustomJsonResponse(data={'total_answers': total_answers})


class CountTotalAnswersForQuestionAPIView(APIView):
    def post(self, request, room_id, question_id, *args, **kwargs):
        data = request.data

        user_id = data['user_id']

        total_answers = GameAnswer.objects.filter(room_id=room_id, player_id=user_id, question_id=question_id).count()

        return CustomJsonResponse(data={'total_answers': total_answers})


class TimerAPIView(APIView):
    def get(self, request, room_id, user_id, *args, **kwargs):
        game_room = GameRoom.objects.get(id=room_id)
        game_questions = game_room.questions.all()
        player = Player.objects.get(id=user_id)

        seconds_from_start = (datetime.now() - game_room.started_at.replace(tzinfo=None)).seconds
        if 0 <= seconds_from_start < 15:
            seconds_left = 15 - seconds_from_start
            question = game_questions[0]
        elif 15 <= seconds_from_start < 18:
            seconds_left = 0
            question = game_questions[0]
        elif 18 <= seconds_from_start < 33:
            seconds_left = 33 - seconds_from_start
            question = game_questions[1]
        elif 33 <= seconds_from_start < 36:
            seconds_left = 0
            question = game_questions[1]
        elif 36 <= seconds_from_start < 51:
            seconds_left = 51 - seconds_from_start
            question = game_questions[2]
        else:
            seconds_left = 0
            question = game_questions[2]

        if game_room.creator == player:
            opponent = game_room.opponent
        else:
            opponent = game_room.creator

        opponent_answer = GameAnswer.objects.filter(room=game_room, player=opponent, question=question).first()
        opponent_answer = AnswerSerializer(opponent_answer.answer).data if opponent_answer else None

        data = {
            'seconds_left': seconds_left,
            'current_question_id': question.id,
            'opponent_answer': opponent_answer,
        }

        return CustomJsonResponse(data=data)
