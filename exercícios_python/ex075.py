num = (int(input("Digite um  número: ")),
       int(input("Digite um  número: ")),
       int(input("Digite um  número: ")),
       int(input("Digite um  número: ")))

print(f'Você digitou os valores {num}')
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print("O valor 3 não apareceu em nenhuma posição.")

print('Os valores pares digitados foram:', end=' ')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
