from math import factorial

num = int(input("Digite um número para saber seu fatorial: "))
f = factorial(num)
c = num

print("Calculando {}! = ".format(num), end=" ")

while c > 0:
    print(f"{c}", end=" ")
    print(" x " if c > 1 else ' = ', end=" ")
    c -= 1
print(f"{f}")
