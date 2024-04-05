from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Empresa
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer

from django.views.decorators.csrf import csrf_exempt


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


@api_view(['POST'])
def cadastrar_empresa(request):
    if request.method == 'POST':
        nome = request.data.get('nome')

        if not nome:
            return Response({'mensagem': 'Todos os campos são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            empresa = Empresa.objects.create(nome=nome)
            return Response({'mensagem': 'Empresa cadastrado com sucesso'}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'mensagem': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Se a solicitação não for POST, retorne uma resposta indicando que o método não é permitido
    return Response({'mensagem': 'Método não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
