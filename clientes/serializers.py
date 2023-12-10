from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import * # o asteristico diz o que está no arquivo será importado


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})
        return data

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não Insira numero nesse campo'})
        return data

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"Insira o restante do digitos"})
        return data
    
        if not celular_valido(data['celular']):
            raise serializers.ValidationError("Insira o numero do seu celular corretamente")

