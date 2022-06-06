from django.urls import path
from .views import MeasureView

urlpatterns = [
    path('measure/', MeasureView.as_view(),),
    path('measure/<str:measure_id>/', MeasureView.as_view()),
]