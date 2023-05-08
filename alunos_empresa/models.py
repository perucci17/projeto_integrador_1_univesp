

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = (
        ('ALUNO', 'Aluno'),
        ('EMPRESA', 'Empresa'),
    )
    data_criação = models.DateTimeField (auto_now = True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    curso_solicitado = models.CharField (max_length=150)
    observacoes = models.TextField(blank = True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

