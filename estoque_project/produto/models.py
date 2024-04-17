from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    estoque = models.IntegerField()
