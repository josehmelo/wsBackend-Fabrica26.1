from django.db import models


class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'treinadores'
        ordering = ['nome']
        verbose_name = 'Treinador'
        verbose_name_plural = 'Treinadores'

    def __str__(self):
        return self.nome