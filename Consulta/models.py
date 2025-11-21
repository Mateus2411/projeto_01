from django.db import models
from Medico.models import Medico
from Paciente.models import Paciente

# Create your models here.


class Consulta(models.Model):
    data_hora = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Paciente {self.paciente} - {self.data_hora}"
