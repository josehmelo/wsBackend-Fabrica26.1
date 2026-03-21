from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import Treinador
from .serializers import TreinadorSerializer, RegistroSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def registrar_treinador(request):
    serializer = RegistroSerializer(data=request.data)
    if serializer.is_valid():
        treinador = serializer.save()
        refresh = RefreshToken.for_user(treinador)
        return Response({
            'mensagem': 'Treinador registrado com sucesso',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    senha = request.data.get('senha')

    try:
        treinador = Treinador.objects.get(email=email)
    except Treinador.DoesNotExist:
        return Response(
            {'erro': 'Credenciais inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not check_password(senha, treinador.senha):
        return Response(
            {'erro': 'Credenciais inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(treinador)
    return Response({
        'mensagem': f'Bem-vindo, {treinador.nome}!',
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil(request):
    treinador = Treinador.objects.get(email=request.user.email)
    serializer = TreinadorSerializer(treinador)
    return Response(serializer.data)

# Create your views here.
