from rest_framework import serializers
from .models import Treinador


class TreinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinador
        fields = ['id', 'nome', 'idade', 'email', 'data_cadastro']


class RegistroSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Treinador
        fields = ['nome', 'idade', 'email', 'senha']

    def create(self, validated_data):
        from django.contrib.auth.hashers import make_password
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)