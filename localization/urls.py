from django.urls import path
from .views import LocalizationViews,LocalizationOneViews

urlpatterns = [
    path('localization/', LocalizationViews().as_view(),),
    path('localization/<str:localization_id>/', LocalizationOneViews.as_view()),
]