from django.db import models
from barbershop.models import serviceBarbershop
from django.conf import settings


class agenda(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='agendaUsuario')
    responsible = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='responsavelService')
    date = models.DateField()
    hours = models.TimeField()
    service = models.ForeignKey(
        serviceBarbershop, on_delete=models.PROTECT, related_name='servicoUsuario')

    def __str__(self):
        return f'agenda de {self.client.username}'
