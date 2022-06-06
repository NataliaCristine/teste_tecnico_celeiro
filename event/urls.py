from django.urls import path
from .views import EventView

urlpatterns = [
    path('event/', EventView.as_view(),),
    path('event/<str:event_id>/', EventView.as_view()),
]