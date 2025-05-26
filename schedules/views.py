from .models import agenda
from rest_framework import generics
from .serializer import AgendaSerializer


class agendaCriarListarView(generics.ListCreateAPIView):
    queryset = agenda.objects.all()
    serializer_class = AgendaSerializer
