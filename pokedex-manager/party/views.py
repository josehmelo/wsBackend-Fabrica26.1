from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Party
from .serializers import PartySerializer
from services.pokeapi import buscar_pokemon
from treinadores.models import Treinador

@api_view(['GET'])
@permission_classes([AllowAny])
def listar_party(request, treinador_id):
    try:
        treinador = Treinador.objects.get(pk=treinador_id)
    except Treinador.DoesNotExist:
        return Response(
            {'erro': 'Treinador não encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    party = Party.objects.filter(treinador=treinador)
    serializer = PartySerializer(party, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def adicionar_pokemon(request, treinador_id):
    try:
        treinador = Treinador.objects.get(pk=treinador_id)
    except Treinador.DoesNotExist:
        return Response(
            {'erro': 'Treinador não encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    nome_pokemon = request.data.get('pokemon')
    if not nome_pokemon:
        return Response(
            {'erro': 'Informe o nome ou id do pokemon'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if Party.objects.filter(treinador=treinador).count() >= 6:
        return Response(
            {'erro': 'A party já está cheia (máximo 6 pokémons)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    dados = buscar_pokemon(nome_pokemon)
    if not dados:
        return Response(
            {'erro': 'Pokémon não encontrado na PokeAPI'},
            status=status.HTTP_404_NOT_FOUND
        )

    pokemon = Party.objects.create(
        treinador=treinador,
        pokemon_id=dados['id'],
        pokemon_name=dados['nome'],
        pokemon_tipo=dados['tipo'],
        pokemon_imagem_url=dados['imagem_url'],
        anotacoes=request.data.get('anotacoes', ''),
    )

    serializer = PartySerializer(pokemon)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def remover_pokemon(request, treinador_id, pokemon_pk):
    try:
        pokemon = Party.objects.get(pk=pokemon_pk, treinador_id=treinador_id)
    except Party.DoesNotExist:
        return Response(
            {'erro': 'Pokémon não encontrado na party'},
            status=status.HTTP_404_NOT_FOUND
        )

    pokemon.delete()
    return Response(
        {'mensagem': 'Pokémon removido da party!'},
        status=status.HTTP_200_OK
    )


@api_view(['PATCH'])
@permission_classes([AllowAny])
def atualizar_anotacoes(request, treinador_id, pokemon_pk):
    try:
        pokemon = Party.objects.get(pk=pokemon_pk, treinador_id=treinador_id)
    except Party.DoesNotExist:
        return Response(
            {'erro': 'Pokémon não encontrado na party'},
            status=status.HTTP_404_NOT_FOUND
        )

    anotacoes = request.data.get('anotacoes', '')
    pokemon.anotacoes = anotacoes
    pokemon.save()

    serializer = PartySerializer(pokemon)
    return Response(serializer.data)
# Create your views here.
