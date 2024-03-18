# Escreva um programaque leia dois numeros. IMprima o resultado da multiplicaçao do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado

p = int(input("Digite o primeiro numero:"))
s = int(input("Digite o segundo numero:"))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
    print(f" {p} x {s} = {r}")
