import os
import django
from datetime import datetime, date

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from Especialidade.models import Especialidade
from Medico.models import Medico
from Paciente.models import Paciente
from Medicamento.models import Medicamento
from Consulta.models import Consulta
from Receita.models import Receita
from Receita_Medicamento.models import ReceitaMedicamento


def populate_data():
    print("Limpando dados existentes...")
    ReceitaMedicamento.objects.all().delete()
    Receita.objects.all().delete()
    Consulta.objects.all().delete()
    Medicamento.objects.all().delete()
    Medico.objects.all().delete()
    Paciente.objects.all().delete()
    Especialidade.objects.all().delete()

    print("Criando especialidades...")
    especialidades = [
        Especialidade.objects.create(nome="Cardiologia"),
        Especialidade.objects.create(nome="Dermatologia"),
        Especialidade.objects.create(nome="Ortopedia"),
        Especialidade.objects.create(nome="Pediatria"),
        Especialidade.objects.create(nome="Ginecologia"),
    ]

    print("Criando medicos...")
    medicos = [
        Medico.objects.create(
            nome="Dr. Joao Silva", crm="12345", especialidade=especialidades[0]
        ),
        Medico.objects.create(
            nome="Dra. Maria Santos", crm="23456", especialidade=especialidades[1]
        ),
        Medico.objects.create(
            nome="Dr. Pedro Costa", crm="34567", especialidade=especialidades[2]
        ),
        Medico.objects.create(
            nome="Dra. Ana Lima", crm="45678", especialidade=especialidades[3]
        ),
        Medico.objects.create(
            nome="Dr. Carlos Souza", crm="56789", especialidade=especialidades[4]
        ),
    ]

    print("Criando pacientes...")
    pacientes = [
        Paciente.objects.create(
            nome="Jose Oliveira", data_nascimento=date(1985, 3, 15)
        ),
        Paciente.objects.create(
            nome="Maria Fernandes", data_nascimento=date(1992, 7, 22)
        ),
        Paciente.objects.create(
            nome="Carlos Pereira", data_nascimento=date(1978, 11, 8)
        ),
    ]

    print("Criando medicamentos...")
    medicamentos = []
    nomes_medicamentos = [
        ["Aspirina", "Losartana", "Atorvastatina", "Enalapril", "Digoxina"],
        ["Cetoconazol", "Tacrolimus", "Retinoide", "Hidrocortisona", "Clotrimazol"],
        ["Ibuprofeno", "Paracetamol", "Diclofenaco", "Naproxeno", "Celecoxib"],
        [
            "Amoxicilina",
            "Azitromicina",
            "Ibuprofeno Infantil",
            "Paracetamol Infantil",
            "Dipirona",
        ],
        ["Progesterona", "Estrogenio", "Misoprostol", "Mifepristona", "Contraceptivo"],
    ]

    dosagens = ["100mg", "50mg", "20mg", "10mg", "5mg"]

    for i, especialidade in enumerate(especialidades):
        for j, nome in enumerate(nomes_medicamentos[i]):
            medicamentos.append(
                Medicamento.objects.create(
                    nome=nome,
                    descricao=f"Medicamento para {especialidade.nome}",
                    dosagem=dosagens[j],
                    especialidade=especialidade,
                )
            )

    print("Criando consultas...")
    consultas = []
    for i in range(5):
        consultas.append(
            Consulta.objects.create(
                medico=medicos[i % len(medicos)],
                paciente=pacientes[i % len(pacientes)],
                data_hora=datetime.now(),
            )
        )

    print("Criando receitas...")
    receitas = []
    for consulta in consultas:
        receitas.append(Receita.objects.create(consulta=consulta, data=datetime.now()))

    print("Criando prescricoes...")
    for i, receita in enumerate(receitas):
        # Cada receita tera 1-3 medicamentos da especialidade do medico
        especialidade_medico = receita.consulta.medico.especialidade
        meds_disponiveis = list(
            Medicamento.objects.filter(especialidade=especialidade_medico)
        )

        num_meds = min(3, len(meds_disponiveis))
        for j in range(num_meds):
            ReceitaMedicamento.objects.create(
                receita=receita,
                medicamento=meds_disponiveis[j],
                quantidade=(j + 1) * 10,  # 10, 20, 30 unidades
            )

    print("Dados populados com sucesso!")
    print(f"Estatisticas:")
    print(f"- {Especialidade.objects.count()} especialidades")
    print(f"- {Medico.objects.count()} medicos")
    print(f"- {Paciente.objects.count()} pacientes")
    print(f"- {Medicamento.objects.count()} medicamentos")
    print(f"- {Consulta.objects.count()} consultas")
    print(f"- {Receita.objects.count()} receitas")
    print(f"- {ReceitaMedicamento.objects.count()} prescricoes")


if __name__ == "__main__":
    populate_data()
