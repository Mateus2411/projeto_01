from rest_framework import viewsets
from .models import ReceitaMedicamento
from .serializers import ReceitaMedicamentoSerializer


class ReceitaMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer
