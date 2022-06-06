from dataclasses import fields
from rest_framework import serializers
from .models import Localization

class LocalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Localization
        fields = ['uuid', 'city']
        read_only_fields = ['uuid']