from django.db import models
from treinadores.models import Treinador

class Party(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name='party')
    pokemon_id = models.IntegerField()
    pokemon_name = models.CharField(max_length=100)
    pokemon_tipo = models.CharField(max_length=50)
    pokemon_imagem_url = models.URLField(blank=True, null=True)
    data_captura = models.DateTimeField(auto_now_add=True)
    anotacoes = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'party'
        ordering = ['pokemon_name']
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'
        
    def __str__(self):
        return f'{self.pokemon_name}, capturado por {self.treinador.nome}'

# Create your models here.
