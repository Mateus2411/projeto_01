from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome