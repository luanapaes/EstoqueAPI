from django.db import models
from empresa.models import Empresa


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    tipo = models.CharField(max_length=10, choices=[
        ('ADM', 'Administrador'), ('FUNC', 'Funcionário Comum')])
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=255, null=True, blank=True)