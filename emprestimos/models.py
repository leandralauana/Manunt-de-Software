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

    def __str__(self):
        return f'{self.livro.titulo} emprestado para {self.usuario.nome}'
