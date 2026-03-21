from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_treinador, name='registro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]