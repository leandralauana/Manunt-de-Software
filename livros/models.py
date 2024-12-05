from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
    