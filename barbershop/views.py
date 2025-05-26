from django.shortcuts import render
from rest_framework import generics
from .models import Barbershop, serviceBarbershop
from .serializer import barbershopsSerializer, serviceSerializer


class barbershopCreateListView(generics.ListCreateAPIView):
    queryset = Barbershop.objects.all()
    serializer_class = barbershopsSerializer


class serviceCreateListView(generics.ListCreateAPIView):
    queryset = serviceBarbershop.objects.all()
    serializer_class = serviceSerializer
