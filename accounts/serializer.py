from rest_framework import serializers
from .models import usuarioVisitante


class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = usuarioVisitante
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = usuarioVisitante.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
