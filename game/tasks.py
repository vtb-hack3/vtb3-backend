from datetime import datetime, timedelta
from game.models import GameRoom


def make_room_unjoinable():
    GameRoom.objects.filter(created_at__lte=datetime.now() - timedelta(seconds=30)).update(is_joinable=False)
