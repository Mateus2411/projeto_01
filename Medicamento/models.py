from django.db import models
from Especialidade.models import Especialidade

# Create your models here.

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    dosagem = models.CharField(max_length=50)
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome
