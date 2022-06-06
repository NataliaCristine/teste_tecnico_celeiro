from django.urls import path
from .views import GameView

urlpatterns = [
    path('game/', GameView.as_view(),),
    path('game/<str:game_id>/', GameView.as_view()),
]