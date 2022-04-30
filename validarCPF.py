cpf = '59218283355'
guardar_valid = []
controle = 10
controle2 = 0
soma = 0
primeiroDigito = 0

print('1° validação')
print()

for numero in cpf[:9]:
    print(f'{numero} * {controle} = {int(numero)* controle}')
    guardar_valid.append(int(numero) * controle)
    soma += guardar_valid[controle2]
    controle -=1
    controle2 +=1

print(f'resultado da multiplicação = {soma}')

verificarPrimeiroDigito = (soma*10)%11
primeiroDigito = verificarPrimeiroDigito
if verificarPrimeiroDigito >=10:
    primeiroDigito = 0

print()
print(f'Digito verificador ENCONTRADO = {primeiroDigito}')
print(f'Digito verificador DIGITADO = {cpf[9:10]}')
print()


if int(cpf[9:10]) == primeiroDigito:
    print('2° validação')

    # reiniciando as variaveis
    controle = 11
    controle2 = 0
    guardar_valid = []
    soma = 0
    for numero in cpf[:10]:
        print(f'{numero} * {controle} = {int(numero) * controle}')
        guardar_valid.append(int(numero) * controle)
        soma += guardar_valid[controle2]
        controle -= 1
        controle2 += 1

print(f'resultado da multiplicação = {soma}')
verificarSegundoDigito = (soma*10)%11
segundoDigito = verificarSegundoDigito
if verificarSegundoDigito >=10:
    segundoDigito = 0

print()
print(f'Digito verificador ENCONTRADO = {segundoDigito}')
print(f'Digito verificador DIGITADO = {cpf[10:11]}')
print()

if primeiroDigito == int(cpf[9:10]) and segundoDigito == int(cpf[10:11]):
    print('CPF informado é VÁLIDO!')
else:
    print('CPF informado é INVÁLIDO!')