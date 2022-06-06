from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import LocalizationSerializer
from .models import Localization


class LocalizationViews(ListCreateAPIView):

    queryset= Localization.objects.all()
    serializer_class= LocalizationSerializer

class LocalizationOneViews(RetrieveUpdateDestroyAPIView):

    queryset= Localization.objects.all()
    serializer_class= LocalizationSerializer

    lookup_url_kwarg = 'localization_id'
    lookup_field = 'uuid'