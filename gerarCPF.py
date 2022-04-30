from random import randint

cpf = str(randint(100000000,999999999))
print(cpf)
guardar_valid = []
controle = 10
controle2 = 0
soma = 0
primeiroDigito = 0

for numero in cpf:
  guardar_valid.append(int(numero) * controle)
  soma += guardar_valid[controle2]
  controle -=1
  controle2 +=1

verificarPrimeiroDigito = (soma*10)%11
if verificarPrimeiroDigito > 9:
   cpf += str(0)
else:
   cpf += str(verificarPrimeiroDigito)

print(cpf)
controle = 11
controle2 = 0
guardar_valid = []
soma = 0
for numero in cpf:
 guardar_valid.append(int(numero) * controle)
 soma += guardar_valid[controle2]
 controle -= 1
 controle2 += 1

verificarSegundoDigito = (soma*10)%11
if verificarSegundoDigito > 9:
   cpf +=str(0)
else:
   cpf += str(verificarSegundoDigito)

print(cpf)
