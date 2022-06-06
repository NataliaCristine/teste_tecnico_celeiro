
from rest_framework import serializers
from user.serializers import UserSerializer
from game.serializer import GameSerializer
from localization.serializer import LocalizationSerializer

class EventSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name= serializers.CharField()
    sport = serializers.CharField()
    localization = LocalizationSerializer(read_only=True)
    users =UserSerializer(many=True,read_only=True)
    game = GameSerializer(read_only=True)

class EventSerializerUpdate(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name= serializers.CharField(required = False)
    sport = serializers.CharField(required = False)
    localization = LocalizationSerializer(read_only=True)
    users =UserSerializer(many=True,read_only=True)
    game = GameSerializer(read_only=True)