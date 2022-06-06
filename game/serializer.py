from rest_framework import serializers
from team.serializer import TeamSerializer

class GameSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name =serializers.CharField()
    year =serializers.IntegerField()
    season=serializers.CharField()
    teams =TeamSerializer(many=True,read_only=True)

class GameSerializerUpdate(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name =serializers.CharField(required=False)
    year =serializers.IntegerField(required=False)
    season=serializers.CharField(required=False)
    teams =TeamSerializer(many=True,read_only=True)
