from rest_framework import serializers
from funcionario.models import Funcionario
from empresa.models import Empresa

class FuncionarioSerializer(serializers.ModelSerializer):
    nome_empresa = serializers.CharField(max_length=255)

    class Meta:
        model = Funcionario
        fields = ('id', 'nome', 'email', 'senha', 'tipo', 'nome_empresa')
        read_only_fields = ('empresa',)  # torna o campo apenas leitura

    def validate_nome_empresa(self, value):
        try:
            empresa = Empresa.objects.get(nome=value)
            return empresa.nome
        except Empresa.DoesNotExist:
            raise serializers.ValidationError("A empresa não existe.")

    def create(self, validated_data):
        nome_empresa = validated_data.pop('nome_empresa')

        # busca a empresa com base no nome fornecido
        empresa = Empresa.objects.get(nome=nome_empresa)

        # define o objeto empresa no validated_data antes de criar o funcionário
        validated_data['empresa'] = empresa

        # defina o nome da empresa no campo nome_empresa - preenche na tabela auto
        validated_data['nome_empresa'] = nome_empresa

        return Funcionario.objects.create(**validated_data)
