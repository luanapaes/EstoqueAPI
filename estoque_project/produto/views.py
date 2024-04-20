from django.shortcuts import render
from rest_framework import viewsets
from produto.models import Produto
from produto.serializers import ProdutoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- lista os produto = http://127.0.0.1:8000/api/produtos -----------------------------------------------------------------
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# ----- cadastrar produto ----------------------------------------------------------------------------------------------------
@api_view(['POST'])
def cadastrar_produto(request):
    serializer = ProdutoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'mensagem': 'Produto cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- editar produto----------------------------------------------------------------------------------------------------
@api_view(['PUT'])
def editar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(pk=produto_id)
    except Produto.DoesNotExist:
        return Response({'mensagem': 'produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProdutoSerializer(
        produto, data=request.data, partial=True)
    if serializer.is_valid():

        # cria uma cópia dos dados do funcionário antes da edição
        produto_data_before_edit = ProdutoSerializer(produto).data

        serializer.save()

        # verifica se houve alteração nos dados do funcionário
        produto_data_after_edit = ProdutoSerializer(
            Produto.objects.get(pk=produto_id)).data
        if produto_data_before_edit != produto_data_after_edit:
            return Response({'mensagem': 'Produto editado com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response({'mensagem': 'Nenhum campo foi editado.'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- deletar produto -------------------------------------------------------------------------------------------------


@api_view(['DELETE'])
def excluir_produto(request, produto_id):
    try:
        # verifica se o funcionário existe pelo ID
        produto = Produto.objects.get(pk=produto_id)
    except Produto.DoesNotExist:
        return Response({'mensagem': 'Produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    produto.delete()
    return Response({'mensagem': 'Funcionário excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
