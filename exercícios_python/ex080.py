lista = []

for v in range(0, 5):
    num = int(input("Digite um valor: "))
    if v == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Valor adicionado na {pos}ª posição")
                break
            pos += 1

print(f'Os valores digitados foram {lista[:]}')
