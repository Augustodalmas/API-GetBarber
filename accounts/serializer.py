from rest_framework import serializers
from .models import usuarioVisitante, employee
import re
import dns.resolver


class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = usuarioVisitante
        fields = ['username', 'password', 'password1', 'email']

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                "As senhas não estão iguais!"
            )
        return data

    def validate_password(self, data):
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if not re.match(regex, data):
            raise serializers.ValidationError(
                "A senha deve ter no mínimo 8 caracteres, incluindo uma letra maiúscula, "
                "uma minúscula, um número e um caractere especial (@$!%*?&)."
            )

        return

    def validate_email(self, data):
        dominio = data.split('@')[1]
        try:
            registro_mx = dns.resolver.resolve(dominio, "MX")
            if not registro_mx:
                raise serializers.ValidationError(
                    f'Este dominio de email é inexistente, tem certeza que deseja usar @{dominio}!'
                )

        except Exception:
            raise serializers.ValidationError(
                f'Este dominio de email é inexistente, tem certeza que deseja usar @{dominio}!'
            )

        if usuarioVisitante.objects.filter(email=data).exists():
            raise serializers.ValidationError(
                "Este email já está em uso!"
            )
        return data

    def validate_username(self, data):

        if usuarioVisitante.objects.filter(username=data).exists():
            raise serializers.ValidationError(
                "Este nome de usuário já está em uso!"
            )
        return data

    def create(self, validated_data):
        validated_data.pop('password1')
        user = usuarioVisitante.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class perfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarioVisitante
        fields = ['id', 'username', 'email', 'telefone', 'historico']


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"
