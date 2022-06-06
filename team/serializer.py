from rest_framework import serializers
from user.serializers import UserSerializer

class TeamSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    ndc = serializers.CharField()
    users = UserSerializer(many=True,read_only=True)

class TeamSerializerUpdate(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(required=False)
    ndc = serializers.CharField(required=False)
    users = UserSerializer(many=True,read_only=True)