from rest_framework import viewsets
from .models import Emprestimo
from .serializers import EmprestimoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
