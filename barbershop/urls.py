from django.urls import path, include
from api.views import HelloWorldView

urlpatterns = [
    path('barbershop/hello', HelloWorldView.as_view()),
]
