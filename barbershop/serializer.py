from .models import Barbershop, serviceBarbershop
from rest_framework import serializers


class barbershopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbershop
        fields = "__all__"


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = serviceBarbershop
        fields = "__all__"
