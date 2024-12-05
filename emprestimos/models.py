from django.db import models
from livros.models import Livro
from usuarios.models import Usuario
from django.utils.timezone import now

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    devolvido = models.BooleanField(default=False)

    def dar_baixa(self):
        if not self.devolvido:
            self.devolvido = True
            self.data_devolucao = now()
            self.livro.disponivel = True
            self.livro.save()
            self.save()
