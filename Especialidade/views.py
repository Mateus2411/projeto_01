from rest_framework import viewsets
from .models import Especialidade
from .serializers import EspecialidadeSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
