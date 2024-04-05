from .serializers import FuncionarioSerializer
from .models import Funcionario
from empresa.models import Empresa
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


# views.py

# @api_view(['POST'])
# def cadastrar_funcionario(request):
#     if request.method == 'POST':
#         serializer = FuncionarioSerializer(data=request.data)
#         if serializer.is_valid():
#             nome = serializer.validated_data.get('nome')
#             email = serializer.validated_data.get('email')
#             tipo = serializer.validated_data.get('tipo')
#             empresa = serializer.validated_data.get('empresa')
#             nome_empresa = serializer.validated_data.get('nome_empresa')

#             funcionario = Funcionario.objects.create(
#                 nome=nome, email=email, tipo=tipo, empresa=empresa, nome_empresa=nome_empresa)
#             if funcionario:
#                 return Response({'mensagem': 'Funcionário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'mensagem': 'Falha ao cadastrar funcionário. Esta empresa não existe no banco.'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------------------------------------------------------------

@api_view(['POST'])
def cadastrar_funcionario(request):
    if request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            nome_empresa = serializer.validated_data.get('nome_empresa')

            # verifica se o nome da empresa existe
            try:
                empresa = Empresa.objects.get(nome=nome_empresa)
            except Empresa.DoesNotExist:
                return Response({'mensagem': 'A empresa não existe.'}, status=status.HTTP_400_BAD_REQUEST)

            # se a empresa existe, o serializer já associou a empresa ao funcionário
            funcionario = serializer.save()

            if funcionario:
                nome_empresa = request.data.get('nome_empresa')
                return Response({'mensagem': 'Funcionário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'mensagem': 'Falha ao cadastrar funcionário.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
