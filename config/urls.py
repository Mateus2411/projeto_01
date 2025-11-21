"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Especialidade.views import EspecialidadeViewSet
from Medico.views import MedicoViewSet
from Paciente.views import PacienteViewSet
from Consulta.views import ConsultaViewSet
from Medicamento.views import MedicamentoViewSet
from Receita.views import ReceitaViewSet
from Receita_Medicamento.views import ReceitaMedicamentoViewSet

router = DefaultRouter()
router.register(r"especialidades", EspecialidadeViewSet)
router.register(r"medicos", MedicoViewSet)
router.register(r"pacientes", PacienteViewSet)
router.register(r"consultas", ConsultaViewSet)
router.register(r"medicamentos", MedicamentoViewSet)
router.register(r"receitas", ReceitaViewSet)
router.register(r"receita-medicamentos", ReceitaMedicamentoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
