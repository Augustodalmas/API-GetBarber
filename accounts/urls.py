from django.urls import path, include
from api.views import HelloWorldView

urlpatterns = [
    path('accounts/hello', HelloWorldView.as_view()),
]
