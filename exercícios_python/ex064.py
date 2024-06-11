count = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input("Digite um número  [999 para parar]: "))
    if numero != 999:
        count += 1
        soma += numero
    else:
        break
print(f"Você digitou {count} números e a soma entre eles foi {soma}")