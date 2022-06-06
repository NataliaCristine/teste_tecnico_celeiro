from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name =serializers.CharField()
    sex = serializers.CharField()
    

class UserSerializerUpdate(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name =serializers.CharField(required=False)
    sex = serializers.CharField(required=False)

   