total_saques = {k1:v1, k2:v2, k3:v3}
lim_valores = len(total_saques.values())
saque = list(total_saques.keys())
s_saldo =- t_saldo
d_saldo =+ t_saldo
t_saldo = s_saldo + d_saldo

while lim_valores <= 500:
    try:
        = int(input(f"Digite a quantia que gostaria de sacar: "))
        for saque in t_saldo:
            print(f'Seu saldo atual é: {s_saldo}')
    except:
        print ("Por favor, tente novamente")
        continue
    else:
        print ("Obrigado por digitar um número!")
        break
    finally:
        print("Fim da execução!")

employees = {}

for i in range(3):
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")

    employees[name] = salary


# 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
print(employees)

total_saq = {'saque1':1.05, 'saque2':4.00, 'saque3':8.00}
total_dep = {'deposito1':1.00,'deposito2':2.00, 'deposito3':3.00}


s_saldo =- sum(list(total_saq.values()))
d_saldo =+ sum(list(total_dep.values()))
t_saldo = s_saldo + d_saldo


print(f'Valor de saques: R${round((s_saldo),2)}')
print(f'Valor de depósito: R${round((d_saldo),2)}')
print(f'Valor total do saldo: R${round((t_saldo),2)}')

saq = {'saque1':valor1, 'saque2':valor2, 'saque3':valor3}

saq1 = float(input('Digite o primeiro valor de saque: '))
saq2 = float(input('Digite o segundo valor de saque: '))
saq3 = float(input('Digite o terceiro valor de saque: '))
print(f'Primeiro valor de saque: R${saq1}')
print(f'Segundo valor de saque: R${saq2}')
print(f'Terceiro valor de saque: R${saq3}')

saq

lim_val = list(saq.values())

lim_val

for i in lim_val:
    if i < 500:
        print(f'Valor R${i} retirado.')
    else:
        print(f'O valor R${i} de saque não foi autorizdo. O valor maximo por saque é R$500.00')

v_saq1 = float(input('Digite o primeiro valor de saque: '))
v_saq2 = float(input('Digite o segundo valor de saque: '))
v_saq3 = float(input('Digite o terceiro valor de saque: '))

print(f'Primeiro valor de saque: R${v_saq1}')
print(f'Segundo valor de saque: R${v_saq2}')
print(f'Terceiro valor de saque: R${v_saq3}')

for i in lim_val:
    if i < 500:
        print(f'Valor R${i} retirado.')
    else:
        print(f'O valor R${i} de saque não foi autorizdo. O valor maximo por saque é R$500.00')

dep = {'deposito1':v_dep1,'deposito2':v_dep2, 'deposito3':v_dep3}
d_saldo = sum(list(dep.values()))
v_dep1 = float(input('Digite o primeiro valor de deposito: '))
v_dep2 = float(input('Digite o segundo valor de deposito: '))
v_dep3 = float(input('Digite o terceiro valor de deposito: '))

dep

for k,i in dep:
    print(f'Seu saldo atual é: {d_saldo}')