valor = []
maior = menor = 0
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        if valor[cont] < menor:
            menor = valor[cont]

print('=-' * 20)
print(f'Você digitou os valores {valor}')
print(f"O maior valor foi {maior} nas posições ", end='')
for indice, v in enumerate(valor):
    if v == maior:
        print(f'{indice}...', end='')
print()
print(f"E o menor valor foi {menor} nas posições ", end='')
for indice, v in enumerate(valor):
    if v == menor:
        print(f'{indice}...', end='')
print()
