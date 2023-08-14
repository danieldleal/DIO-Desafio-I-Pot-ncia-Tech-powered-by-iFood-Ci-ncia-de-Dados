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
- [07.08.2023] |(Day 1) 1.0 -> Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
- [08.08.2023] | Desenvolvimento da função 2 e 3 do sistema bancário
_____________________________________________________________________
To-Do:
- Redigir Pseudocódigo e estudar funções cabíveis para o desafio;
- Desmembrar os trechos de código para o saque, depósito e extrato bancário de modo a otimizar o sistema e relacionar as variáveis entre si;
_____________________________________________________________________
Pseudo-code:
1. Imprimir a mensagem de boas vindas
2. Imprimir as opções e para o usuário digitar qual delas deve ser
3. Função saque:
    3.1 Saques que, somados não podem, dar mais que 500 reais e também não pode até 3
    3.2 Ter uma funcao somatório que calcule a soma de cada agregando ao valor total
    3.3 Criação de uma variável para cada valor que não pode ser permitido (saque não permitido para valores R$500.00)
4. Função depósito:
    4.1 Variável para somatório de todos os depósitos
    4.2 Não há necessidade de explicitar um usuário
5. Função extrato:
    5.1 Se não houve uso das funções saque e depósito, imprimir que não houve movimentações na sessão.

_____________________________________________________________________
Autor: Daniel Leal (desafio DIO)"""

# 1. Imprimir para selecionar as opções:

escolha = int
(input
 ('''
  
  *** Bem vindo ao nosso sistema bancário ***

  Escolha a opção desejada:              
    1 - Função saque
    2 - Função depósito
    3 - Extrato bancário
  
  '''))

# 2. Escolher a função:

def escolha(int):
    while True:
        try:
            if escolha == int(1):
                print('Você escolheu a função saque!')
            elif escolha == int(2):
                print('Você escolheu a função depósito!')
            elif escolha == int(3):
                print('Você escolheu a função extrato bancário!')
        except:
            print ("Você não digitou um número!")
            continue
        finally:
            print("Obrigado por escolher o nosso banco. Fim da execução!")

# 2.1. Função saque:
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, 
# o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

while max(max_val) <= 500.00:
    try:
        saq = {'saque1':v_saq1, 'saque2':v_saq2, 'saque3':v_saq3}
        max_val = max(list(saq.values()))
        s_saldo = sum(list(saq.values()))
        v_saq1 = float(input('Digite o primeiro valor de saque: '))
        v_saq2 = float(input('Digite o segundo valor de saque: '))
        v_saq3 = float(input('Digite o terceiro valor de saque: '))
        for i in max_val:
            if i < 500:
                print(f'Valor R${i} retirado.')
            else:
                print(f'O valor R${i} de saque não foi autorizado. O valor maximo por saque é R$500.00')
                str(input('Gostaria de fazer um novo saque? '))
                pass
    except:
        print ("Por favor, tente novamente")
        escolha()
        continue
    finally:
        print(f'O total de sacado foi: R$ {s_saldo}')
        print('Obrigado por utilizar nosso serviço.')
        break

# 2.2. Função depósito:
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, 
# dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

dep = {}
for k,v in dep:
    try:
        dep = {'deposito1':v_dep1,'deposito2':v_dep2, 'deposito3':v_dep3}
        d_saldo = sum(list(dep.values()))
        v_dep1 = float(input('Digite o primeiro valor de saque: '))
        v_dep2 = float(input('Digite o segundo valor de saque: '))
        v_dep3 = float(input('Digite o terceiro valor de saque: '))
        for k,i in dep:
            print(f'Seu saldo atual é: {d_saldo}')
            continue
        else:
            print('Por favor, tente novamente.')
    except:
        print ("Por favor, tente novamente")
        escolha()
        continue
    finally:
        print(f'O total depositado foi: R$ {d_saldo}')
        print('Obrigado por utilizar nosso serviço.')
        break

# 2.3. Função extrato bancário:
# Essa operação deve listar todos os depósitos e saques realizados na conta. 
# No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

t_saldo = d_saldo - s_saldo

if d_saldo and s_saldo == 0:
    print('Não foram realizadas movimentações nesta sessão.')

print
(f'''
  *** Bem vindo ao nosso sistema bancário ***
  As suas operações foram:
 
    1.Operações de saque:
    Primeiro valor de saque: R$ {v_saq1}
    Segundo valor de saque: R$ {v_saq2}
    Terceiro valor de saque: R$ {v_saq3}
    O total sacado foi: R$ {s_saldo}
    
    2. Operações de depósito:
    Primeiro valor de deposito: R$ {v_dep1}
    Segundo valor de deposito: R$ {v_dep2}
    Terceiro valor de deposito: R$ {v_dep3}
    O total depositado foi: R$ {d_saldo}

    O valor total em conta é: R$ {round(t_saldo, 2)}
''')

print('Obrigado por utilizar nosso serviço.')