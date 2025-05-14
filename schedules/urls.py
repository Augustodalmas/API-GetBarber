from django.urls import path, include
from api.views import HelloWorldView

urlpatterns = [
    path('schedules/hello', HelloWorldView.as_view()),
]