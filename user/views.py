import random
from rest_framework.views import APIView


# Create your views here.
from user.models import Player
from user.serializers import PlayerSerializer
from utils.api import CustomJsonResponse


class CreateUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.pop('name')
        player, _ = Player.objects.update_or_create(name=name, defaults=data)

        return CustomJsonResponse(data=PlayerSerializer(player).data)


class UserTopAPIView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        return CustomJsonResponse(data={'top': random.randint(1, 5)})
