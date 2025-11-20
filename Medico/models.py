from django.db import models
from Especialidade.models import Especialidade

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nome} ({self.crm}) - {self.especialidade}"
