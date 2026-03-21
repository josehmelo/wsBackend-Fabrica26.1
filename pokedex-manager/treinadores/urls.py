from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_treinador, name='registro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    
     path('', views.listar_treinadores, name='listar_treinadores'),
    path('novo/', views.criar_treinador, name='criar_treinador'),
    path('<int:pk>/editar/', views.editar_treinador, name='editar_treinador'),
    path('<int:pk>/deletar/', views.deletar_treinador, name='deletar_treinador'),
]