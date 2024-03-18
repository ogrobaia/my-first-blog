# Escreva um programa que leia dois numeros e que pergunte qual a operação voce deseja realizar . Voce deve poder calcuilar soma , subtração 
# multiplicação e divisao . Exiba o resultado da operação.

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
operacao = input("Qual operação deseja realizar? (, - , * ou  / ) :")

if operacao == "+":
   resultado = a + b
elif operacao == "-":
   resultado = a - b
elif operacao == "*":
   resultado = a * b
elif operacao == "/":
   resultado = a / b
else:
   print("Digite um dos numeros informados para a operação ")
   Resultado = 0
print("O resultado da operação é:" , resultado)



# a = float(input("Primeiro número:"))
# b = float(input("Segundo número:"))
# operação = input("Digite a operação a realizar (+, -, * ou /):")
# if operação == "+":
#     resultado = a + b
# elif operação == "-":
#     resultado = a - b
# elif operação == "*":
#     resultado = a * b
# elif operação == "/":
#     resultado = a / b
# else:
#     print("Operação inválida!")
#     resultado = 0
# print("Resultado: ", resultado)