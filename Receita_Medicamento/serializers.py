from rest_framework import serializers
from .models import ReceitaMedicamento
from Medicamento.models import Medicamento

class ReceitaMedicamentoSerializer(serializers.ModelSerializer):
    medicamentos_disponiveis = serializers.SerializerMethodField()

    class Meta:
        model = ReceitaMedicamento
        fields = '__all__'

    def get_medicamentos_disponiveis(self, obj):
        try:
            especialidade_medico = obj.receita.consulta.medico.especialidade
            medicamentos = Medicamento.objects.filter(especialidade=especialidade_medico).values('id', 'nome')
            return list(medicamentos)
        except AttributeError:
            return []
