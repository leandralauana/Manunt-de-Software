from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Emprestimo
from .serializers import EmprestimoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    @action(detail=True, methods=['post'])
    def dar_baixa(self, request, pk=None):
        """
        Endpoint para marcar o empréstimo como devolvido.
        """
        try:
            emprestimo = self.get_object()
            if emprestimo.devolvido:
                return Response({'detail': 'Este empréstimo já foi devolvido.'}, status=status.HTTP_400_BAD_REQUEST)

            emprestimo.dar_baixa()
            return Response({'detail': 'Baixa realizada com sucesso.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
