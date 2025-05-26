from .models import agenda
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = agenda
        fields = "__all__"

    def validate(self, data):

        date = data.get('date')
        hours = data.get('hours')
        responsible = data.get('responsible')

        if agenda.objects.filter(date=date, hours=hours, responsible=responsible).exists():
            raise serializers.ValidationError(
                "Já existe um serviço com este Responsável no mesmo horário e data!"
            )

        return data
