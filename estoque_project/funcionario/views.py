from .serializers import FuncionarioSerializer
from .models import Funcionario
from empresa.models import Empresa
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

# ---------------------------------------------------------------------------------------------
def generate_unique_username(nome):
    # Gera um nome de usuário único a partir do nome do funcionário.

    username = nome.lower().replace(' ', '_')
    i = 1
    while User.objects.filter(username=username).exists():
        username = f'{username}_{i}'
        i += 1
    return username

# ---------------------------------------------------------------------------------------------
@api_view(['POST'])
def cadastrar_funcionario(request):
    serializer = FuncionarioSerializer(data=request.data)
    if serializer.is_valid():
        nome_empresa = serializer.validated_data.get('nome_empresa')

        # verifica se o nome da empresa existe
        try:
            empresa = Empresa.objects.get(nome=nome_empresa)
        except Empresa.DoesNotExist:
            return Response({'mensagem': 'A empresa não existe.'}, status=status.HTTP_400_BAD_REQUEST)

        # se a empresa existe, associa-a ao funcionário para salvar só depois das validações
        serializer.validated_data['empresa'] = empresa

        # cria uma cópia dos dados do funcionário 
        funcionario_data = serializer.validated_data.copy()

        # verifica se o email já está cadastrado
        if User.objects.filter(email=funcionario_data['email']).exists():
            return Response({'mensagem': 'Já existe um usuário com este email.'}, status=status.HTTP_400_BAD_REQUEST)

        # verifica o tipo de usuário
        if funcionario_data['tipo'] not in ['ADM', 'FUNC']:
            return Response({'mensagem': 'Tipo de usuário inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        # gera um nome de usuário único com a função
        username = generate_unique_username(funcionario_data['nome'])

        # cria o usuário
        user = User.objects.create_user(
            username=username,
            email=funcionario_data['email'],
            password=funcionario_data['senha'],
        )

        # salva o funcionário no banco
        funcionario = serializer.save()
        if funcionario:
            # atribui o usuário ao funcionário
            funcionario.user = user
            funcionario.save()

            return Response({'mensagem': 'Funcionário cadastrado com sucesso.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'mensagem': 'Falha ao cadastrar funcionário.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---------------------------------------------------------------------------------------------
@api_view(['POST'])
def fazer_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('senha')

        if not email or not password:
            return Response({'mensagem': 'Email e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # verifica se o e-mail está cadastrado
            funcionario = Funcionario.objects.get(email=email)
        except Funcionario.DoesNotExist:
            return Response({'mensagem': 'Email e senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)

        # verifica se a senha combina com o e-mail cadastrado
        if (password == funcionario.senha): #verifica se a senha inserida é a mesma guardada no banco
            return Response({'mensagem': 'Login realizado com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'mensagem': 'E-mail ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)
        
# -------------------------------------------------------------------------------------------------------------
@api_view(['PUT'])
def editar_funcionario(request, funcionario_id):
    try:
        funcionario = Funcionario.objects.get(pk=funcionario_id)
    except Funcionario.DoesNotExist:
        return Response({'mensagem': 'Funcionário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FuncionarioSerializer(
        funcionario, data=request.data, partial=True)
    if serializer.is_valid():

        # cria uma cópia dos dados do funcionário antes da edição
        funcionario_data_before_edit = FuncionarioSerializer(funcionario).data

        serializer.save()

        # verifica se houve alteração nos dados do funcionário
        funcionario_data_after_edit = FuncionarioSerializer(
            Funcionario.objects.get(pk=funcionario_id)).data
        if funcionario_data_before_edit != funcionario_data_after_edit:
            return Response({'mensagem': 'Funcionário editado com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response({'mensagem': 'Nenhum campo foi editado.'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------------------------------------------------------------
@api_view(['DELETE'])
def excluir_funcionario(request, funcionario_id):
    try:
        funcionario = Funcionario.objects.get(pk=funcionario_id) # verifica se o funcionário existe pelo ID
    except Funcionario.DoesNotExist:
        return Response({'mensagem': 'Funcionário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    funcionario.delete()
    return Response({'mensagem': 'Funcionário excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
