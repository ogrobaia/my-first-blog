# Tabuada tradicional
n = int(input("Tabuada de:"))
x = 1
 
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1

# Tabuada Customizada 

n = int(input("Tabuada de:"))
x = int(input("Digite o inicio da tabuada:"))
fim = int(input("Digite o Fim da Tabuada: "))
 
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
