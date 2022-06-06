from django.urls import path
from .views import TeamView

urlpatterns = [
    path('team/', TeamView.as_view(),),
    path('team/<str:team_id>/', TeamView.as_view()),
]