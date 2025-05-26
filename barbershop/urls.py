from django.urls import path, include
from .views import barbershopCreateListView, serviceCreateListView

urlpatterns = [
    path('barbershop/', barbershopCreateListView.as_view(),
         name='create-list-barbershop'),
    path('barbershop/service/', serviceCreateListView.as_view(),
         name='create-list-service'),
]
