from rest_framework import serializers

from user.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ('created_at', )
