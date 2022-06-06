from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/', UserView.as_view(),),
    path('user/<str:user_id>/', UserView.as_view()),
    
]