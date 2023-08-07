### Sistema bancário ###

# -*- coding: utf-8 -*-
__title__ = "Sistema bancário"
__doc__ = """Version = 1.0
Date    = 07.08.2023
_____________________________________________________________________
Descrição/Objetivo:
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
_____________________________________________________________________
Como:
-> Em desenvolvimento
_____________________________________________________________________
Updates:
- [07.08.2023] | 1.0 (Day 1) -> Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

_____________________________________________________________________
To-Do:
- Pseudocódigo
- 
_____________________________________________________________________
Pseudo-code:
1. Imprimir a mensagem de boas vindas
2. Imprimir as opções e para o usuário digitar qual delas deve ser
3. Código para função saque:
    3.1 

_____________________________________________________________________
Autor: Daniel Leal (desafio DIO)"""

# 1. Imprimir para selelecionar as opções:


print('Bem vindo ao nosso banco:')

escolha = print(input('Escolha a opção desejada:'))

# 2. Escolher a função:
# 2.1. Função saque:
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, 
# o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

    if escolha == int(1):
    print('Você escolheu a função saque')


# 2.2. Função depósito:
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, 
# dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.







# 2.3. Função extrato bancário:
# Essa operação deve listar todos os depósitos e saques realizados na conta. 
# No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

