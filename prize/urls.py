from django.urls import path
from .views import PrizeView

urlpatterns = [
    path('prize/', PrizeView.as_view(),),
    path('prize/<str:prize_id>/', PrizeView.as_view()),
]