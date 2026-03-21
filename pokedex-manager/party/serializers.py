from rest_framework import serializers
from .models import Party 

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'id',
            'treinador',
            'pokemon_id',
            'pokemon_name',
            'pokemon_tipo',
            'pokemon_imagem_url',
            'data_captura',
            'anotacoes',
        ]
        read_only_fields = ['treinador', 'data_captura']