from django.shortcuts import render
from rest_framework import viewsets
from produto.models import Produto
from produto.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
