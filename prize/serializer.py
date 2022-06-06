from rest_framework import serializers
from user.serializers import UserSerializer
from event.serializer import EventSerializer


class PrizeSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    medal = serializers.CharField()
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)