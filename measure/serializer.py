
from rest_framework import serializers
from user.serializers import UserSerializer

class MeasureSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    heigth= serializers.IntegerField(required=False)
    wheight=serializers.IntegerField(required=False)
    age = serializers.CharField(required=False)
    user = UserSerializer(read_only=True)