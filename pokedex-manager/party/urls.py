from django.urls import path
from . import views

urlpatterns = [
    path('<int:treinador_id>/', views.listar_party, name='listar_party'),
    path('<int:treinador_id>/adicionar/', views.adicionar_pokemon, name='adicionar_pokemon'),
    path('<int:treinador_id>/remover/<int:pokemon_pk>/', views.remover_pokemon, name='remover_pokemon'),
    path('<int:treinador_id>/atualizar/<int:pokemon_pk>/', views.atualizar_anotacoes_api, name='atualizar_anotacoes_api'),
    
    path('<int:treinador_id>/', views.listar_party, name='listar_party'),
    path('<int:treinador_id>/adicionar/', views.adicionar_pokemon, name='adicionar_pokemon'),
    path('<int:treinador_id>/remover/<int:pokemon_pk>/', views.remover_pokemon, name='remover_pokemon'),
]