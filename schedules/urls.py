from django.urls import path, include
from .views import agendaCriarListarView

urlpatterns = [
    path('schedules/', agendaCriarListarView.as_view(),
         name='create-list-schedule'),
]
