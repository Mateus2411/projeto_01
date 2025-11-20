from django.db import models
from Receita.models import Receita
from Medicamento.models import Medicamento

# Create your models here.

class ReceitaMedicamento(models.Model):
    receita = models.ForeignKey(
        Receita,
        on_delete=models.CASCADE
    )
    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE
    )
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.medicamento.nome}"