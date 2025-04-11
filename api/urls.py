from django.urls import path, include
from api.views import HelloWorldView

urlpatterns = [
    path('hello', HelloWorldView.as_view()),
]
