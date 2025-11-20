from django.db import models
from Consulta.models import Consulta
# Create your models here.

class Receita(models.Model):
    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE
    )
    data = models.DateTimeField()

    def __str__(self):
        return f"Receita {self.id}"