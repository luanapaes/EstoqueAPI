from rest_framework import serializers
from funcionario.models import Funcionario
from empresa.models import Empresa


# class FuncionarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Funcionario
#         fields = ('id', 'nome', 'email', 'tipo', 'empresa', 'nome_empresa')

class FuncionarioSerializer(serializers.ModelSerializer):
    nome_empresa = serializers.CharField(max_length=255)

    class Meta:
        model = Funcionario
        fields = ('id', 'nome', 'email', 'tipo', 'nome_empresa')
        read_only_fields = ('empresa',)  # apenas leitura do id empresa

    def create(self, validated_data):
        nome_empresa = validated_data.pop('nome_empresa')

        # busca a empresa com base no nome fornecido na hora do cadastro
        empresa = Empresa.objects.get(nome=nome_empresa)

        # Define o objeto empresa no validated_data antes de criar o funcionário
        validated_data['empresa'] = empresa
        return Funcionario.objects.create(**validated_data)
