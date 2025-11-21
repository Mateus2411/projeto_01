import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from Receita_Medicamento.models import ReceitaMedicamento
from Receita_Medicamento.serializers import ReceitaMedicamentoSerializer
import json

print("Testando API - medicamentos_disponiveis")
print("=" * 50)

# Testar com diferentes especialidades
especialidades = [
    "Cardiologia",
    "Dermatologia",
    "Ortopedia",
    "Pediatria",
    "Ginecologia",
]

for esp in especialidades:
    rm = ReceitaMedicamento.objects.filter(
        receita__consulta__medico__especialidade__nome=esp
    ).first()

    if rm:
        serializer = ReceitaMedicamentoSerializer(rm)
        meds = serializer.data["medicamentos_disponiveis"]
        print(f"\n{esp}: {len(meds)} medicamentos")
        for med in meds[:3]:  # Mostrar apenas os primeiros 3
            print(f"  - {med['nome']} (ID: {med['id']})")
        if len(meds) > 3:
            print(f"  ... e mais {len(meds) - 3} medicamentos")
    else:
        print(f"\n{esp}: Nenhum registro encontrado")

print("\n" + "=" * 50)
print("Teste concluído!")
